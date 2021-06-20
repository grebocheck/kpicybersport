from django.urls import path
from . import views
from django.contrib import auth
from datetime import datetime
from django.conf.urls import url
from django.views.generic.base import RedirectView
from articles.models import Article
from tournament.models import Tournament
from django.contrib.sitemaps import views as sitemap_views    # Представление 
from django.contrib.sitemaps import GenericSitemap            # Шаблонный класс для формирования страницы Sitemap
from django.views.decorators.cache import cache_page          # Декоратор кеширования

info_articles = {
        'queryset': Article.objects.all(),
        'date_field': 'post_date',
    }

info_tournaments = {
        'queryset': Tournament.objects.all(),
        'date_field': 'post_date',
    }

sitemaps = {'aricles': GenericSitemap(info_articles, priority=0.5),
            'tournaments': GenericSitemap(info_tournaments, priority=0.7),
            'home': views.HomeSitemap
            }

urlpatterns = [
    url(r'^sitemap\.xml$', cache_page(86400)(sitemap_views.index), {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>\w+)\.xml$', cache_page(86400)(sitemap_views.sitemap), {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path(''        , views.index   , name='home'),
    path('about/'  , views.about   , name='about'),
    path('contact/', views.contact , name='contact'),
    path('profile/', views.profile , name='profile'),
    path('profile/edit_profile', views.edit_profile , name='edit_profile'),
    path('register/', views.register, name='register'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico'), name='favicon'),
    path('forgot_password/', views.forgot_password , name='forgot_password'),
    path('forgot_password/reset_password', views.reset_mail , name='reset_mail'),
    path('reset_pass/<str:token>/', views.new_password, name='new_password'),
    path('reset_pass/<str:token>/reset', views.reset_pass, name='reset_pass'),
]