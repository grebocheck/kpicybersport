from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.http import HttpRequest
from .models import Abou , Contact , Imagin , Topx , Person
from articles.models import Article
from main.forms import UserRegistrationForm

def index(request):
    try:
        a = Topx.objects.all()
        b1 = a[0].top_article
        b2 = a[1].top_article
        b3 = a[2].top_article
        print(a[0].top_article.imagin1)
    except:
        b1 = ''
        b2 = ''
        b3 = ''
        print("ERORR: Виберіть статті на головну сторінку")

    try:
        a = Imagin.objects.all()
        ib = a[0].imagin_url
        ic = a[1].imagin_url
        id = a[2].imagin_url
        tb = a[0].title
        tc = a[1].title
        td = a[2].title
        xb = a[0].texte
        xc = a[1].texte
        xd = a[2].texte
        bb = a[0].bath_title
        bc = a[1].bath_title
        bd = a[2].bath_title
        ub = a[0].batn_url
        uc = a[1].batn_url
        ud = a[2].batn_url
    except:
        ib = ""
        ic = ""
        id = ""
        tb = ""
        tc = ""
        td = ""
        xb = ""
        xc = ""
        xd = ""
        bb = ""
        bc = ""
        bd = ""
        ub = ""
        uc = ""
        ud = ""
    return render(request , 'main/index.html'  , {'year':datetime.now().year ,
                                                 'imagin1': ib , 'imagin2': ic , 'imagin3': id,
                                                 'title1' : tb , 'title2' : tc , 'title3' : td ,
                                                 'text1'  : xb ,'text2'   : xc ,'text3'   : xd ,
                                                 'btnt1'  : bb ,'btnt2'   : bc ,'btnt3'   : bd ,
                                                 'urlb1'  : ub ,'urlb2'   : uc ,'urlb3'   : ud ,
                                                 'article1' : b1 , 'article2' :b2 , 'article3':b3,
                                                  })

def about(request):
    try:
        a = Abou.objects.all()
        b = a[0].about_text
    except:
        b = "Опис відсутній"
    return render(request , 'main/about.html'  , {'year':datetime.now().year ,'about_text': b })

def contact(request):
    try:
        a = Contact.objects.all()
        b = a[0].contact_text
    except:
        b = "Контакти відсутні"
    return render(request , 'main/contact.html', {'year':datetime.now().year ,'contact_text': b})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Створеня моделі профіля для нового користувача
            person = Person.objects.create(user=new_user , player_name='',steam_link = '' ,vuz='',fuck='',group='',rate='')
            person.save()
            return render(request, 'main/register_done.html', {'year':datetime.now().year,'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'year':datetime.now().year,'user_form': user_form})


def profile(request):
    if request.user.username == "":
        return render(request, 'main/n_profile.html',{'year':datetime.now().year})
    else:
        try:
            a = Person.objects.get(user = request.user)
        except:
            raise Http404("Профіль не знайдено")
        return render(request, 'main/profile.html',{'year':datetime.now().year , 'profile':a})

def edit_profile(request):
    try:
        a = Person.objects.get(user = request.user)
    except:
        raise Http404("Профіль не знайдено")
    player_name_new = request.POST['player_name']
    steam_link_new = request.POST['steam_link']
    vuz_new = request.POST['vuz']
    fuck_new = request.POST['fuck']
    group_new = request.POST['group']
    rate_new = request.POST['rate']
    if player_name_new:
        a.player_name = player_name_new
    if steam_link_new:
        a.steam_link = steam_link_new
    if vuz_new:
        a.vuz = vuz_new
    if group_new:
        a.group = group_new
    if rate_new:
        a.rate = rate_new
    a.save()
    return render(request, 'main/profile.html',{'year':datetime.now().year , 'profile':a})

def sitemap(request):
    """Renders the sitemap page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sitemap.xml',
        {
            'title':'Плани на сайт',
            'message':'Heridium site description',
            'year':datetime.now().year,
        }
    )

    sponseRedirect(reverse('articles:detail' , args = (a.id,)))