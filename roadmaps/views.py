from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages

from django_table_sort.table import TableSort
from django_tables2 import RequestConfig

from .models import Trajectory, TrajElement
from .tables import CourseTable


class IndexView(generic.ListView):
    template_name = 'roadmaps/index.html'
    context_object_name = 'trajectory_list'

    def get_queryset(self):
        return Trajectory.objects.all()[:10]


class TrajectoryView(generic.DetailView):
    model = Trajectory
    template_name = 'roadmaps/trajectory.html'


class ElementView(generic.DetailView):
    model = TrajElement
    template_name = 'roadmaps/element.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = CourseTable(
            context['trajelement'].courses.all(),
            empty_text = 'Курсов по элементу не найдено.'
            )
        RequestConfig(self.request).configure(table)
        context['coursetable'] = table
        return context


def toggle_element(request, pk):
    elem = TrajElement.objects.get(id=pk)
    if elem in request.user.profile.completed_elements.all():
        request.user.profile.completed_elements.remove(elem)
        messages.success(request, 'Элемент отмечен как выполненный.')
    else:
        request.user.profile.completed_elements.add(elem)
        messages.success(request, 'Элемент отмечен как невыполненный.')
    request.user.save()
    return redirect(reverse('roadmaps:trajectory', args=[elem.trajectory.slug]))
