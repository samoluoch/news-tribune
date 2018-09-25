from django.contrib import admin
from .models import Editor,Article,Tags

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    # The class ArticleAdmin inherits from the ModelAdmin class. This class allows us to edit our models from the admin page. We then specify the filter_horizontal property that allows ordering of many to many fields and pass in the tags article field that helps in editing the tags area.


admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)