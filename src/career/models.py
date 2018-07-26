from django.db import models
from beema.models import TimeStampedModel, GenericModel


class Vacancy(GenericModel):

    class meta:
        verbose_name = "Vacency"
        verbose_name_plural = "Vacencies"



class Result(GenericModel):
    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"


class ExamForm(GenericModel):
    class Meta:
        verbose_name = "Exam Form"
        verbose_name_plural = "Exam forms"
