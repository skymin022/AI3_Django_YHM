from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('create/', views.create, name='create'),
    path('read/<int:no>/', views.read, name='read'),  # 상세
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('ing/', views.mark_ing, name='ing'),
    path('done/', views.toggle_complete, name='toggle_complete'),
]
