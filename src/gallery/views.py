from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import PhotoGallery, VideoGallery


def photo_gallery(request):
    """photo gallery"""
    galleries = get_list_or_404(PhotoGallery)
    return render(request, 'gallery/photo_gallery.html', {
        "galleries": galleries
    })


def video_gallery(request):
    """Render video gallery"""
    galleries = get_list_or_404(VideoGallery)
    return render(request, 'gallery/video_gallery.html', {
        "galleries": galleries

    })


def photo_gallery_detail(request, title, pk):
    """Render the photo gallery"""
    gallery = get_object_or_404(PhotoGallery, pk=pk)

    return render(request, 'gallery/photo_gallery_detail.html', {
        "gallery": gallery
    })


def video_gallery_detail(request, title, pk):
    """
    Render the video detail.
    """
    gallery = get_object_or_404(VideoGallery, pk=pk)

    return render(request, 'gallery/video_gallery_detail.html', {
        "gallery": gallery
    })
