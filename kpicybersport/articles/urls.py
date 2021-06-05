from django.urls import path
from . import views


app_name='articles'

urlpatterns = [
    path(''        , views.list   , name='list'),
    path('<int:article_id>/', views.single, name='single'),
    path('<int:article_id>/leave_comment', views.leave_comment , name = 'leave_comment'),
]