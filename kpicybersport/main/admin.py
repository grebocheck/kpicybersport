from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Abou , Contact , Imagin , Topx , Downl , Person

class AbouModelAdmin(admin.ModelAdmin):
    list_display = ["id" , "about_text"]
    class Meta:
        model=Abou

admin.site.register(Abou , AbouModelAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id" , "contact_text"]
    class Meta:
        model=Contact

admin.site.register(Contact , ContactModelAdmin)

class ImaginModelAdmin(admin.ModelAdmin):
    list_display = ["id" , "imagin_url"]
    class Meta:
        model=Imagin

admin.site.register(Imagin , ImaginModelAdmin)

class TopxModelAdmin(admin.ModelAdmin):
    list_display = ["id" , 'top_article']
    class Meta:
        model=Topx

admin.site.register(Topx , TopxModelAdmin)

class DownlModelAdmin(admin.ModelAdmin):
    list_display = ["id" , 'filer']
    class Meta:
        model=Downl

admin.site.register(Downl , DownlModelAdmin)

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["user" , 'player_name']
    class Meta:
        model=Person

admin.site.register(Person , PersonModelAdmin)