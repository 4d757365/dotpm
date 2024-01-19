from django.urls import path

from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add_project'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit_project, name='edit_project'),
    path('<uuid:pk>/delete/', views.delete_project, name='delete_project'),
    path('<uuid:project_id>/files/upload/',
         views.upload_file, name='upload_file'),
    path('<uuid:project_id>/files/<uuid:pk>/delete/',
         views.delete_file, name='delete_file'),
    path('<uuid:project_id>/notes/add/', views.add_note, name='add_note'),
    path('<uuid:project_id>/notes/<uuid:pk>/', views.note, name='note'),
    path('<uuid:project_id>/notes/<uuid:pk>/edit/',
         views.edit_note, name='edit_note'),
    path('<uuid:project_id>/notes/<uuid:pk>/delete/',
         views.delete_note, name='delete_note'),
]
