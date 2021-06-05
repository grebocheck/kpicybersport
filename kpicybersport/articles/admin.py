from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Article , Comment
 
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "post_date"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "post_date"]
    search_fields = ["title", "article_text"]
    class Meta:
        model = Article

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
 
admin.site.register(Article , ArticleModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"article", "comment_text", "author" , "date_post"]
    list_filter = ["date_post"]
    class Meta:
        model=Comment

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

admin.site.register(Comment , CommentModelAdmin)