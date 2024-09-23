from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('<int:task_id>/update/', views.update_task, name='update_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
]
