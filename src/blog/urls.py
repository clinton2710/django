#from django.contrib import admin
from django.urls import path
from .views import(
    # aritcle_list_view,
    # aritcle_detial_view
    ArticleListview,
    ArticleDetailview,
    ArticleCreateview,
    ArticleUpdateview,
    ArticleDeleteview
)
app_name = 'blog'
urlpatterns = [
    path('', ArticleListview.as_view(), name= 'article-list'),
    path ('<int:id>/detail/',ArticleDetailview.as_view(), name= "article-detail"),
    path('create/', ArticleCreateview.as_view(), name= 'article-create'),
    path ('<int:id>/update/',ArticleUpdateview.as_view(), name= "article-update"),
    path ('<int:id>/delete/',ArticleDeleteview.as_view(), name= "article-delete"),


]