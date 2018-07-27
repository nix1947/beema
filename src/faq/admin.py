from django.contrib import admin
from .models import FaqCategories, Faq


class FaqInline(admin.StackedInline):
    model = Faq
    list_display = ['title', 'u']


@admin.register(FaqCategories)
class FaqCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_date']
    list_filter = ['title']
    inlines = [FaqInline]



admin.site.register(Faq)