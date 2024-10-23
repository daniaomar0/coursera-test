from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views




urlpatterns = [
    path('<pk>/', views.create_book, name='create-book'),
    path('htmx/book/<pk>/', views.detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', views.update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', views.delete_book, name="delete-book"),
    path('htmx/create-book-form/', views.create_book_form, name='create-book-form'),
]