from django.db import models
from beema.models import TimeStampedModel
from django.urls import reverse
from django.utils.text import slugify


class Gallery(TimeStampedModel):
    gallery_name = models.CharField(max_length=255)
    gallery_cover_photo = models.ImageField("Gallery cover photo")

    class Meta:
        abstract = True
        ordering = ('-updated_date',)


class PhotoGallery(Gallery):

    def __str__(self):
        return self.gallery_name

    def get_absolute_url(self):
        return reverse("gallery:photo_gallery_detail", kwargs={
            "title": slugify(self.gallery_name, allow_unicode=True),
            "pk": self.id
        })

    class Meta:
        verbose_name_plural = "Photo Galleries"
        verbose_name = "Photo Gallery"


class VideoGallery(Gallery):

    def __str__(self):
        return self.gallery_name

    def get_absolute_url(self):
        return reverse("gallery:video_gallery_detail", kwargs={
            "title": slugify(self.gallery_name, allow_unicode=True),
            "pk": self.id
        })

    class Meta:
        verbose_name_plural = "Video Galleries"
        verbose_name_plural = "Video Gallery"


class Photo(models.Model):
    gallery = models.ForeignKey('PhotoGallery', related_name="photos", on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="upload/photos")
    caption = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.caption


class Video(TimeStampedModel):
    gallery = models.ForeignKey("VideoGallery", on_delete=models.SET_NULL, null=True, related_name="videos")
    caption = models.CharField(blank=True, null=True, max_length=255)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False, null=False)

    def __str__(self):
        return self.caption
