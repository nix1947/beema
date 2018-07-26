from django.shortcuts import render
from .models import Vacancy, Result, ExamForm
from django.utils.translation import ugettext as _


def vacenceis(request):
    return render(request, "career/career_base.html", {
        "title": _("Vacencies"),
        "objects": Vacancy.objects.filter(draft=False)
    })


def results(request):
    return render(request, "career/career_base.html", {
        "title": _("Results"),
        "objects": Result.objects.filter(draft=False)
    })


def examform(request):
    return render(request, "career/career_base.html", {
        "title": _("Exam Form"),
        "objects": ExamForm.objects.filter(draft=False)
    })
