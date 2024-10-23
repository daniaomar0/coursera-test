from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('community/', views.community, name='community'),
    path('community/create/', views.create_post, name='create_post'),
    path('community/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
