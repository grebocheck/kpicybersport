from django.urls import path
from . import views
from django.contrib import auth
from datetime import datetime
from django.conf.urls import url
from django.views.generic.base import RedirectView
from articles.models import Article
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap


info_articles = {
        'queryset': Article.objects.all(),
        'date_field': 'post_date',
    }

urlpatterns = [
    path('sitemap.xml', sitemap,
            {'sitemaps': {'aricles': GenericSitemap(info_articles, priority=0.6) , }},
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