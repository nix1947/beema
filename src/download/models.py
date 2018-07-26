from django.db import models
from beema.models import TimeStampedModel
from django.urls import reverse

"""
Download Models.
Download category
"""


class DownloadCategory(TimeStampedModel):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


    def get_absolute_url(self):
        return reverse("download:download_category_detail",kwargs={
            'pk': self.pk
        })


class Download(TimeStampedModel):
    """
    """
    download_category = models.ForeignKey(DownloadCategory, related_name="downloads", on_delete=models.SET_NULL,
                                          null=True, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="uploads", verbose_name="Upload File")

    def __str__(self):
        return self.title
