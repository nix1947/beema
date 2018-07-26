from django.shortcuts import render
from .models import DownloadCategory, Download
from django.shortcuts import get_object_or_404


def download_categories(request):
    download_categories = DownloadCategory.objects.order_by('-updated_date')
    return render(request, 'download/download_categories.html', {
        'download_categories': download_categories
    })


def download_categories_detail(request, pk):
    download_category = get_object_or_404(DownloadCategory, pk=pk)
    download_categories = DownloadCategory.objects.order_by('-updated_date')

    # download_categories = DownloadCategory.objects.order_by('-updated_date')
    return render(request, 'download/download_category_detail.html', {
        'category': download_category,
        'download_categories': download_categories
    })
