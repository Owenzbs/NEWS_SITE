from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Comments
from .forms import NewsForm, CommentsForm
from django.db.models import F


# Create your views here.
def index(request):
    news=News.objects.all()
    comments=Comments.objects.all()
    return render(request, 'news/index.html', {'news': news, 'comments': comments, }, )


def view_news(request, news_id):
    news_item=News.objects.get(pk=news_id)
    comments=Comments.objects.all()
    votes=news_item.amount_of_upvotes
    news_item.amount_of_upvotes=F('amount_of_upvotes') + 1
    news_item.save()
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            author_name_new=form.cleaned_data['author_name']
            content_new=form.cleaned_data['content']
            Comments.objects.create(author_name=author_name_new, content=content_new, news_id=news_item.id)
            news_item.amount_of_upvotes=+1
            news_item.save()
    else:
        form=CommentsForm()
    return render(request, 'news/view_news.html', {'news_item':news_item, 'form':form, 'comments':comments, 'news_id':news_id, 'votes':votes})
    


def create_news(request):
    
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            title_new=form.cleaned_data['title']
            link_new=form.cleaned_data['link']
            author_name_new=form.cleaned_data['author_name']
            News.objects.create(title=title_new,link=link_new,author_name=author_name_new,amount_of_upvotes=0)
            response = redirect('/news/')
            return response
    else:
        form=NewsForm()
    
    return render(request, 'news/create.html', {'form':form})