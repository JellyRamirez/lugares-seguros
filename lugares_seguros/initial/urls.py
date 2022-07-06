from django.urls import path

from initial import views

urlpatterns = [
    path('', views.index, name='index'),
]