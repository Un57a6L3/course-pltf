from django.urls import path

from . import views

app_name = 'roadmaps'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('toggle_element/<int:pk>/', views.toggle_element, name='toggle_element'),
    path('<slug:slug>/', views.TrajectoryView.as_view(), name='trajectory'),
    path('<slug:slug>/<int:pk>/', views.ElementView.as_view(), name='element'),
]
