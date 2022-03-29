from unittest import TestCase
from django.urls import path
from .views import index, create_news, view_news


urlpatterns = [
    path('', index),
    path('create', create_news),
    path('news/<int:news_id>', view_news, name='view_news'),
    ]
