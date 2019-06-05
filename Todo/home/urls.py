from django.urls import path

from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('pending/', views.pending, name="pending"),
    path('completed/', views.completed, name="completed"),
]
