"""
Shared abstract models
"""

from django.db import models


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class GenericModel(TimeStampedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    file = models.FileField(upload_to="uploads")
    draft = models.BooleanField("Draft", default=False)

    class Meta:
        abstract = True
        ordering = ('-updated_date',)
