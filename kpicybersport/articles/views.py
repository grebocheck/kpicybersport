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

from .models import Article , Comment

def list(request):
    posts = Article.objects.all().order_by('-post_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
    context = {
        "posts": paginator.get_page(page),
        'title':"Статті",
        'year':datetime.now().year,
    }
    return render(request, "articles/list.html", context)



def single(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статтю не знайдено")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request , "articles/detail.html" , {"article": a, 'latest_comments_list': latest_comments_list,'title':a.title, 'year':datetime.now().year,'author':a.author ,})

def leave_comment(request , article_id ):
    if request.user.username == "":
        ima = "Невідомий"
    else:
        ima = request.user.username
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статтю не знайдено")
    a.comment_set.create(author = ima, comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('articles:single' , args = (a.id,)))
