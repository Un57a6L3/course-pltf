from django.urls import path

from . import views

app_name = 'authapp'
urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<slug:slug>/', views.TrajectoryView.as_view(), name='trajectory'),
    # path('<slug:slug>/<int:pk>/', views.ElementView.as_view(), name='element'),
]