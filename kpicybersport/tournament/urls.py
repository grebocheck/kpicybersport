from django.urls import path
from . import views


app_name='tournament'

urlpatterns = [
    path(''        , views.list   , name='list'),
    path('<int:tournament_id>/', views.single, name='single'),
    path('<int:tournament_id>/leave_team', views.leave_team , name = 'leave_team'),
    path('<int:tournament_id>/del_team', views.del_team , name = 'del_team'),
    path('<int:tournament_id>/commands', views.commands , name = 'commands'),
]