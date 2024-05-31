from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Trajectory, TrajElement

# def index(request):
#     return render(request, 'roadmaps/index.html')


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
