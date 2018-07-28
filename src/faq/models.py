from django.db import models
from beema.models import TimeStampedModel
from django.urls import reverse


class FaqCategories(TimeStampedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("faq:faq_category", kwargs={
            "pk":self.pk
        })


    class Meta:
        ordering = ('title',)
        verbose_name = "Faq Category"
        verbose_name_plural = "Faq Categories"


class Faq(TimeStampedModel):
    faq_category = models.ForeignKey(FaqCategories, on_delete=models.SET_NULL, related_name="faqs", null=True, blank=False)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-updated_date',)
