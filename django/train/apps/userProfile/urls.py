from django.urls import path
from . import views
from django.views.generic import TemplateView

#profile update settings 
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name='search'),
    path('settings/', views.settings, name='settings'),
    path('account/', views.account, name='account'),
     path('password-change/', views.change_password, name='password_change'),
    path('password-change/done/', TemplateView.as_view(template_name='profile/password_reset_done.html'), name='password_reset_done'),
]
