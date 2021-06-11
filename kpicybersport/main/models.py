from django.db import models
from articles.models import Article
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField


class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    player_name = models.TextField('ПІ')
    steam_link = models.TextField('лінк на steam')
    vuz = models.TextField('університет')
    fuck = models.TextField('університет')
    group = models.TextField('група')
    rate = models.TextField('рейтинг')
    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = 'Профілі'



class Abou(models.Model):
    about_text = RichTextField("Про сайт")
    class Meta:
        verbose_name = "Про сайт"
        verbose_name_plural = 'Про сайт'

class Contact(models.Model):
    contact_text = RichTextField("Контакти")
    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = 'Контакти'

class Imagin(models.Model):
    imagin_url = models.URLField("адреса картинки")
    title = models.TextField("Назва")
    texte = models.TextField("Текст")
    bath_title = models.TextField("Текст кнопки")
    batn_url = models.URLField("Адреса для кнопки")

    class Meta:
        verbose_name = "Картинка на прокрутці"
        verbose_name_plural = 'Картинки на прокруці'

class Topx(models.Model):
    top_article = models.IntegerField('ID статті')
    class Meta:
        verbose_name = "Стаття на головній"
        verbose_name_plural = 'Статті на головній'

class Downl(models.Model):
    filer = models.FileField(upload_to='files')
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = 'Файли'
