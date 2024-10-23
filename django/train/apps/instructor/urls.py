from django.urls import path
from . import views

urlpatterns = [
    path('instructor_form/', views.instructorForm, name="instructor_form"),
    path('inst_signup/', views.instructor_signup_view, name='instructor_signup'),
    path('inst_login/', views.instructor_login_view, name='instructor_login'),
    path('teach/', views.teach_button_view, name='teach_button'),
    path('instructor_home/', views.instructorHome, name="instructor_home"),
]