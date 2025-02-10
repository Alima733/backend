from django.urls import path
from .views import get_articles, get_article_by_id

urlpatterns = [
    path('articles/', get_articles),
    path('articles/<int:id>/', get_article_by_id),
]