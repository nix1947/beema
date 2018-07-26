from django.contrib import admin
from .models import (
DownloadCategory,
Download
)

admin.site.register([Download, DownloadCategory])


# Register your models here.
