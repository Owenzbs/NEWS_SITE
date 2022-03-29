from django.contrib import admin
from .models import News, Comments
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title','link','amount_of_upvotes','created_at', 'author_name', )
    list_display_links=('id','title')
    search_fields=('title',)
    
class CommentsAdmin(admin.ModelAdmin):
    list_display=('id','author_name', 'content','created_at','news')
    list_display_links=('id','author_name')
    search_fields=('author_name',)




admin.site.register(News, NewsAdmin)
admin.site.register(Comments)