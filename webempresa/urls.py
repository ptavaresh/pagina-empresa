"""webempresa URL Configuration

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
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de services
    path('services/', include('services.urls')),  # extrae las urls de core/urls.py
    path('blog/', include('blog.urls')),  # extrae las urls de blog/urls.py
    path('page/', include('pages.urls')),  # extrae las urls de blog/urls.py
    path('contact/', include('contact.urls')),  # extrae las urls de blog/urls.py
    #admin paths
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)