from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Tournament(models.Model):
    title = models.TextField("Назва" , max_length=200)
    keywords = models.CharField('Ключові слова' , max_length=120 , null = False , default = "keywords")
    imagin1 = models.ImageField("Картинка 1",upload_to='articles/' , blank=False, null=False)
    content = RichTextField("Контент")
    post_date = models.DateTimeField("Дата публікації" , auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Редаговано" , auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User , on_delete = models.CASCADE )
    link1 = models.URLField("Кнопка 1", blank=True)
    link1_name = models.TextField("Назва кнопки 1", blank=True)
    link2 = models.URLField("Кнопка 2", blank=True)
    link2_name = models.TextField("Назва кнопки 2", blank=True)
    link3 = models.URLField("Кнопка 3", blank=True)
    link3_name = models.TextField("Назва кнопки 3", blank=True)
    players_osn = models.IntegerField("Кількість учасників (2-5)")
    players_dop = models.IntegerField("Кількість запасних учасників (0-2)")
    deadline_reg = models.DateTimeField('Час закінчення реєстрації')

    def __unicode__(self):
        return self.title
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-post_date"]
        verbose_name = "Турнір"
        verbose_name_plural = 'Турніри'


class Team(models.Model):
    tournament = models.ForeignKey(Tournament , on_delete = models.CASCADE)
    date_post = models.DateTimeField("Дата створення" , auto_now=False, auto_now_add=True)
    team_name = models.TextField("Назва команди",max_length = 100)
    capitan = models.TextField("Капітан")
    team_list = models.TextField("Основні учасники")
    dop_team_list = models.TextField("Запасні учасники")
    contact_capitan = models.TextField('Зв`язок з капітаном', max_length = 200)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = 'Команди'

