from django.shortcuts import render, get_object_or_404
from .models import Faq, FaqCategories

# Create your views here.

def faq(request, pk=None):
    faq_categories = FaqCategories.objects.all()

    if pk is not None:
        faq_category = get_object_or_404(FaqCategories, pk=pk)
    else:
        faq_category = FaqCategories.objects.first()


    return render(request, 'faq/faq.html', {
        "faq_categories": faq_categories,
         "faq_category": faq_category
    })