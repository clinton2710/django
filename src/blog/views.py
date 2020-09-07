from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
# from  django.http import HttpResponse
# from .models import Article
from .forms import Blogpost
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import Blogpost

class ArticleCreateview(CreateView):
    template_name = 'blogs/article_create.html'
    form_class = Blogpost
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListview(ListView):
    template_name = 'blogs/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailview(DetailView):
    template_name = 'blogs/article_detail.html'
    #queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id= id_)



class ArticleUpdateview(UpdateView):
    template_name = 'blogs/article_create.html'
    form_class = Blogpost
    queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
    
        return get_object_or_404(Article, id= id_)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteview(DeleteView):
    template_name = 'blogs/article_delete.html'
    #queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id= id_)

    def get_success_url(self):
        return reverse('blog:article-list')

# Create your views here.

# def aritcle_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         'queryset': queryset
#     }
#     return render(request,"blog/article_list.html", context)



# def aritcle_detial_view(request, my_id):
#     obj = Article.objects.get(id= my_id)
#     context = {
#         'object': obj
#     }
#     return render(request, "blog/article_detail.html", context)
