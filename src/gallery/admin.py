from django.contrib import admin

from .models import (
    VideoGallery, PhotoGallery, Photo, Video
)


class PhotoInline(admin.StackedInline):
    model = Photo


class VideoInline(admin.StackedInline):
    model = Video


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery_name']
    search_fields = ['gallery_name']

    inlines = [
        PhotoInline
    ]


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery_name', 'updated_date']
    search_fields = ['gallery_name']

    inlines = [
        VideoInline
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'updated_date']
    search_fields = ['gallery', 'caption']
    list_filter = ['gallery', 'caption']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'caption']
    search_fields = ['gallery', 'caption']
    list_filter = ['gallery', 'caption']



