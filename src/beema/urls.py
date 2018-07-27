"""beema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Homepage
    url('^$', home_views.index, name="index"),
    path('admin/', admin.site.urls),
    # Download
    path('downloads/', include('download.urls', namespace="download")),
    # Career
    path('career/', include('career.urls', namespace="career")),
    # Faq page
    path('faq/', include('faq.urls', namespace='faq'))




]

if settings.DEBUG:
    # Serve media in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
