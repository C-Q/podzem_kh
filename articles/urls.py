from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles_list, name='articles'),
    path('<str:article_url>/', views.render_article),
]