from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('create/', views.create, name='create'),
    path('read/<int:no>/', views.read, name='read'),  
    path('update/', views.update, name='update'),   
    path('delete/', views.delete, name='delete'),
    path('mark_ing/', views.mark_ing, name='mark_ing'),
    path('toggle_complete/', views.toggle_complete, name='toggle_complete'),
    path('wait/', views.mark_wait, name='wait'),
]
