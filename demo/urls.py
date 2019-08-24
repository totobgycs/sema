from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mock1', views.mock1, name='mock1'),
]
