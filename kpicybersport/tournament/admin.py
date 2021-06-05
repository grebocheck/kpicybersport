from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Tournament , Team
 
class TournamentModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "post_date"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "post_date"]
    search_fields = ["title"]
    class Meta:
        model = Tournament

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
 
admin.site.register(Tournament , TournamentModelAdmin)

class TeamModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"tournament", "contact_capitan", "capitan" , "date_post"]
    list_filter = ["date_post"]
    class Meta:
        model=Team

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

admin.site.register(Team , TeamModelAdmin)