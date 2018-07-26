from django.conf.urls import url, static
from django.urls import path
from .views import (
    vacenceis,
    results,
    examform
)


app_name = "career"

urlpatterns = [
    path('', vacenceis, name="index"),
    path('vacencies/', vacenceis, name="vacencies"),
    path('results/', results, name="results"),
    path('exam-forms/', examform, name="examform"),
]