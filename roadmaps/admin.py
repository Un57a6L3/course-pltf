from django.contrib import admin

from .models import Trajectory, TrajElement, Course, Profile, Group

admin.site.register(Trajectory)
admin.site.register(TrajElement)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Group)

admin.site.site_url = '/roadmaps/'
admin.site.site_header = 'Администрирование платформы'
