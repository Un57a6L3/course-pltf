from django.contrib import admin

from .models import Trajectory, TrajElement, Course

admin.site.register(Trajectory)
admin.site.register(TrajElement)
admin.site.register(Course)
