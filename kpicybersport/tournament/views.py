from django.http import Http404 , HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from main.models import Person
from .models import Tournament , Team

def list(request):
    # отображение листа турниров
    posts = Tournament.objects.all().order_by('-post_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
    context = {
        "posts": paginator.get_page(page),
        'title':"Турніри",
        'year':datetime.now().year,
    }
    return render(request, "tournament/list.html", context)

def single(request , tournament_id):
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("турнір не знайдено")

    #отображение контента в зависимости от прав
    forma = False               # форма заявки
    mess_auth = False           # сообщение о неообходимости авторизацыи
    mess_reg = False            # если заявка подана то ее отображает
    teg = []                    # массив заявок к mess_reg
    
    #if request.user.has_perm('auth.change_user'):
    #    # администратор
    #    forma = True
    #    mess_auth = False
    #    mess_reg = False

    #    # якщо час реєстрацій закінчився то реєстрація буде не можлива
    #    if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
    #        forma = False

    if request.user.username == "":
        # пользователь который не авторизовался
        forma = False
        mess_auth = True
        mess_reg = False

    else:
        # пользователь который авторизовался
        forma = True
        mess_auth = False
        mess_reg = False

        # якщо час реєстрацій закінчився то реєстрація буде не можлива
        if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
            forma = False

        asse = a.team_set.order_by('-id')
        ima = request.user.username
        for r in asse:
            if r.capitan == ima:
                forma = False
                mess_reg = True
                teg.append(r)
        if teg != []:
            forma = False
            mess_reg = True

    latest_team_list = a.team_set.order_by('-id')

    return render(request , "tournament/detail.html" , {"tournament": a,'title':a.title, 'year':datetime.now().year,'author':a.author,'forma':forma,'mess_auth':mess_auth,'mess_reg':mess_reg ,'teg':teg})



def leave_team(request , tournament_id ):
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("турнір не знайдено")

    team_name = request.POST['team_name']
    contact_capitan = request.POST['contact_capitan']
    team_list_s = request.POST['team_list']
    dop_team_list_s = request.POST['dop_team_list']
    capitan = request.user.username

    team_list_m = team_list_s.split()
    dop_team_list_m = dop_team_list_s.split()

    errors = []

    
    #перевірка на те чи зареєстровані користувачі
    for k in team_list_m:
        try:
            b = User.objects.get(username = k)
        except:
            message = f"гравець {k} не зареєстрований"
            errors.append(message)

        #перевірка на те чи капітан не вказаний двічі
        if k == request.user.username:
            message = f"гравець {k} вже вказаний як капітан"
            errors.append(message)
    
    #перевірка на те чи зареєстровані користувачі
    for k in dop_team_list_m:
        try:
            b = User.objects.get(username = k)
        except:
            message = f"гравець {k} не зареєстрований"
            errors.append(message)

        #перевірка на те чи капітан не вказаний двічі
        if k == request.user.username:
            message = f"гравець {k} вже вказаний як капітан"
            errors.append(message)

    #перевірка кількості
    kol = a.players_osn
    if kol != 1+len(team_list_m):
        message = f"вам потрібно вказати лише {kol-1} основних гравців"
        errors.append(message)
    kol_dop = a.players_dop
    if kol_dop < len(dop_team_list_m):
        message = f"вам потрібно вказати не більше {kol-1} запасних гравців"
        errors.append(message)

    #перевірка на повтори
    mass = team_list_m + dop_team_list_m
    set_mass = set(mass)
    print(mass)
    print(set_mass)
    if len(mass) != len(set_mass):
        message = f"гравці не можуть повторюватись"
        errors.append(message)

    #перевірка на дедлайн реєстрації
    if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
        message = f"Період реєстрації закінчився"
        errors.append(message)

    if errors:
        for er in errors:
            messages.error(request, er)
        return HttpResponseRedirect(reverse('tournament:single' , args = (a.id,)))
    else:
        team_list = ' '.join(team_list_m)
        dop_team_list = ' '.join(dop_team_list_m)

        a.team_set.create(team_name = team_name , capitan = capitan , team_list = team_list , dop_team_list = dop_team_list , contact_capitan = contact_capitan)

        return HttpResponseRedirect(reverse('tournament:single' , args = (a.id,)))

def del_team(request , tournament_id ):
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("турнір не знайдено")

    latest_team_list = a.team_set.order_by('-id')

    b = request.user.username
    for k in latest_team_list:
        if k.capitan == b:
            k.delete()

    return HttpResponseRedirect(reverse('tournament:single' , args = (a.id,)))

def commands(request , tournament_id):
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("турнір не знайдено")

    class Cap:
        pass

    commands = a.team_set.order_by('-id')
    for b in commands:
        uchasniki = []
        osn = b.team_list.split(" ")
        dop = b.dop_team_list.split(" ")
        
        cas = Cap()
        cas.name = b.capitan
        cas.role = 'Капітан'
        k = User.objects.get(username = b.capitan)
        pers = Person.objects.get(user=k)
        cas.pri = pers.player_name
        cas.steam = pers.steam_link
        cas.vuz = pers.vuz
        cas.fuck = pers.fuck
        cas.group = pers.group
        cas.rate = pers.rate
        uchasniki.append(cas)

        for c in osn:
            cas = Cap()
            cas.name = c
            cas.role = 'Учасник'
            k = User.objects.get(username = c)
            pers = Person.objects.get(user=k)
            cas.pri = pers.player_name
            cas.steam = pers.steam_link
            cas.vuz = pers.vuz
            cas.fuck = pers.fuck
            cas.group = pers.group
            cas.rate = pers.rate
            uchasniki.append(cas)
           
        for d in dop:
            cas = Cap()
            cas.name = d
            cas.role = 'Запасний'
            k = User.objects.get(username = d)
            pers = Person.objects.get(user=k)
            cas.pri = pers.player_name
            cas.steam = pers.steam_link
            cas.vuz = pers.vuz
            cas.fuck = pers.fuck
            cas.group = pers.group
            cas.rate = pers.rate
            uchasniki.append(cas)

        b.temate = uchasniki

    return render(request , "tournament/commands.html" , {"tournament": a, "commands":commands})