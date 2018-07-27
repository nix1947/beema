from django.urls import path
from .views import faq

app_name = "faq"
urlpatterns = [
    path('', faq, name="faq_categories"),
    path('<int:pk>/', faq, name="faq_category"),
]