"""podzem_kh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="static_pages/index.html"), name='index'),
    path('ancient-dungeon/', TemplateView.as_view(template_name="static_pages/ist_podz.html",
                                                  extra_context={'ist_podz_highlight': "class=active_page"}),
         name='ist_podz'),
    path('cave-quest/', TemplateView.as_view(template_name="static_pages/cave_quest.html",
                                             extra_context={'cave_quest_highlight': "class=active_page"}),
         name='cave_quest'),
    path('booking/', include('booking.urls')),
    path('briefing/', TemplateView.as_view(template_name="static_pages/briefing.html",
                                           extra_context={'briefing_highlight': "class=active_page"}),
         name='briefing'),
    path('safety-rules/', TemplateView.as_view(template_name="static_pages/safety_rules.html",
                                               extra_context={'safety_highlight': "class=active_page"}),
         name='safety_rules'),

    path('articles/', include('articles.urls')),

    path('questions/', TemplateView.as_view(template_name="static_pages/questions.html",
                                            extra_context={'questions_highlight': "class=active_page"}),
         name='questions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
