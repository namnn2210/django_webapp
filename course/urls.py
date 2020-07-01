from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_courses, name='all_courses'),
    path('add', views.add_course, name='add_course'),
    path('search', views.search_courses, name='search_courses'),
    path('edit/<int:course_id>', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>', views.delete_course, name='delete_course')
]
