from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

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

    # # All of the below is code for django-table-sort,
    # # which for some reason did not sort. Yup.
    # # It did add some pretty buttons though
    # 
    # ordering_key = 'o'
    # 
    # def get_ordering(self) -> tuple:
    #     return self.request.GET.getlist(self.ordering_key, None)
    # 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['table'] = TableSort(
    #         self.request,
    #         context['trajelement'].courses.all(),
    #         fields=['name', 'topic', 'language', 'duration', 'difficulty', 'detail', 'userscore'],
    #         sort_key_name=self.ordering_key,
    #         table_css_clases="table table-light table-striped table-sm",
    #     )
    #     return context
