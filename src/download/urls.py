from django.urls import path
from .views import (
    download_categories,
    download_categories_detail
)


app_name = "download"

urlpatterns = [
    path('', download_categories, name="downloads"),
    path('<pk>/', download_categories_detail, name="download_category_detail")
]