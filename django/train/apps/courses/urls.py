from django.urls import path
from . import views

urlpatterns=[
    path('course/<int:course_id>/', views.display_course, name='course'),
    path('courses/', views.courses, name='courses'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('create-course/', views.create_course_step1, name='course_creation'),
    path('add/<int:course_id>/sections/', views.add_sections_lectures, name='add_sections_lectures'),
    path('add-section/<int:course_id>', views.add_section, name='add_section'),
    path('course/add_lecture/<str:section_prefix>/', views.add_lecture, name='add_lecture'),
]