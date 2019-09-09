from django.urls import path

from . import views

urlpatterns = [
    path('mock1', views.view_mock1, name='mock1'),
    path('', views.view_index, name='index'),
    path('<str:label>/', views.view_language, name='language'),
    path('postmessage/<str:label>/', views.view_postmessage, name='postmessage'),
]
