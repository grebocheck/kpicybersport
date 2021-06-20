from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime , timedelta
from django.http import HttpRequest , Http404 , HttpResponseRedirect , HttpResponse
from .models import Abou , Contact , Imagin , Topx , Person , PassToken
from articles.models import Article
from main.forms import UserRegistrationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from django.contrib import messages
from kpicybersport import settings
from pytz import timezone
from django.urls import reverse
from django.contrib import sitemaps

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def index(request):
    try:
        a = Topx.objects.all()
        article1 = Article.objects.get(id = a[0].top_article)
        article2 = Article.objects.get(id = a[1].top_article)
        article3 = Article.objects.get(id = a[2].top_article)
    except:
        article1 = ''
        article2 = ''
        article3 = ''
        print("ERORR: Виберіть статті на головну сторінку")

    try:
        a = Imagin.objects.all()
        imagin1 = a[0]
        imagin2 = a[1]
        imagin3 = a[2]
    except:
        imagin1 = ''
        imagin2 = ''
        imagin3 = ''
    return render(request , 'main/index.html'  , {'year':datetime.now().year ,
                                                  'imagin1':imagin1,
                                                  'imagin2':imagin2,
                                                  'imagin3':imagin3,
                                                  'article1':article1,
                                                  'article2':article2,
                                                  'article3':article3})

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
            person = Person.objects.create(user=new_user , player_name=' ',steam_link = ' ' ,vuz=' ',fuck=' ',group=' ',rate=' ')
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
            print(request.user.username)
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
    if fuck_new:
        a.fuck = fuck_new
    if group_new:
        a.group = group_new
    if rate_new:
        a.rate = rate_new
    a.save()
    return render(request, 'main/profile.html',{'year':datetime.now().year , 'profile':a})

#def sitemap(request):
#    """renders the sitemap page."""
#    assert isinstance(request, httprequest)
#    return render(request,'main/sitemap.xml',{'year':datetime.now().year,})

#    sponseredirect(reverse('articles:detail' , args = (a.id,)))

class HomeSitemap(sitemaps.Sitemap):
    priority = 0.5         # Приоритет
    changefreq = 'daily'   # Частота проверки
 
    # Метод, возвращающий массив с url-ками
    def items(self):
        return ['home', 'contact','about']
 
    # Метод непосредственной экстракции url из шаблона
    def location(self, item):
        return reverse(item)


def reset_mail(request):
    try:
        a = User.objects.get(email = request.POST['email'])
    except:
        raise Http404("Користувача не знайдено")
    times = datetime.now()
    token = ''
    for i in range(32):
        token += random.choice(chars)

    pass_token = PassToken.objects.create(user=a,post_date=times,token=token)
    pass_token.save()
    try:
        send_mail(message=f"""Вітаю {a.username}, Ви ініціювали зміну паролю на сайті {settings.SITE_URL}
        
        
        Якщо це були ви то перейдіть по посиланню {settings.SITE_URL}/reset_pass/{token}""",subject='Зміна паролю', from_email='sitekpicybersport@gmail.com', recipient_list = [a.email])
    except Exception as e:
        print(e)
        return render(request , 'main/error.html'  , {'year':datetime.now().year})
    
    return render(request , 'main/email_send.html'  , {'year':datetime.now().year})


def forgot_password(request):
    return render(request , 'main/forgot_password.html'  , {'year':datetime.now().year})

def new_password(request,token):
    try:
        a = PassToken.objects.get(token=token)
    except:
        return render(request , 'main/token_old.html'  , {'year':datetime.now().year})
    time_now = datetime.now().astimezone(timezone(settings.TIME_ZONE))
    #print(settings.TIME_ZONE)
    #print(time_now-a.post_date)
    if time_now-a.post_date <= timedelta(minutes = 30):
        return render(request , 'main/password_reset.html'  , {'year':datetime.now().year})
    else:
        return render(request , 'main/token_old.html'  , {'year':datetime.now().year})

def reset_pass(request,token):
    try:
        a = PassToken.objects.get(token=token)
    except:
         return render(request , 'main/token_old.html'  , {'year':datetime.now().year})
    time_now = datetime.now().astimezone(timezone(settings.TIME_ZONE))
    if time_now-a.post_date <= timedelta(minutes = 30):
        pass1 = request.POST["new_password"]
        pass2 = request.POST["repit_password"]
        errors = []
        if pass1 != pass2:
            errors.append('Повтор паролю не сбігається з новим паролем')
        if errors:
            for er in errors:
                messages.error(request, er)
            return HttpResponseRedirect(reverse('new_password' , args = (token,)))
        else:
            user = a.user
            user.set_password(pass1)
            user.save()
            a.delete()
            return render(request , 'main/sucess_new_password.html'  , {'year':datetime.now().year})
    else:
        return render(request , 'main/token_old.html'  , {'year':datetime.now().year})

def clen_tokens():
    try:
        tokens = PassToken.objects.all()
        time_now = datetime.now().astimezone(timezone(settings.TIME_ZONE))
        for a in tokens:
            if time_now-a.post_date <= timedelta(minutes = 30):
                a.delete()
    except:
        pass