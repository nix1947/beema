from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path('photo/', views.photo_gallery, name="photo_gallery"),
    path('video/', views.video_gallery, name="video_gallery"),
    # Photo gallery detail
    path('photo/<str:title>/<int:pk>', views.photo_gallery_detail, name="photo_gallery_detail"),
    # Video gallery detail
    path('video/<str:title>/<int:pk>', views.video_gallery_detail, name="video_gallery_detail"),
]