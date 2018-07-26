from django.contrib import admin
from .models import (
    Vacancy,
    ExamForm,
    Result
)


class CareerAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_date', 'file', ]
    search_fields = ['title']



resistered_models = [Vacancy, ExamForm, Result]

admin.site.register(resistered_models, CareerAdmin)
