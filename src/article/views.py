from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy
from article.forms import ArticleModelForm, CommentModelForm 
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()
    paginate_by = 20 
    context_object_name = 'articles'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleModelForm
    login_url = '/users/register/'
    success_url = reverse_lazy('articles') # TO DO: redirect to article detail page 
    template_name = 'article/article_create.html'

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    pk_url_kwarg = 'article_id'
    login_url = '/users/register/'
    context_object_name = 'article'
    form_class = CommentModelForm
    success_url = reverse_lazy('article_detail')
    success_message = 'Your comment has been added successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context

    def form_valid(self,form):
        form.instance.article = self.get_object()
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleModelForm
    login_url = '/users/register/'
    template_name = 'article/article_create.html'
    success_message = 'Article has been updated'
    pk_url_kwarg = 'article_id'
    success_url = reverse_lazy('articles') # TO DO : direct to article_detail
    # Initiate form with current content

class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    pk_url_kwarg = 'article_id'
    login_url = '/users/register/'
    success_message = 'The article has been deleted successfully'
    success_url = reverse_lazy('articles')

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request,messages.INFO,self.success_message)
        return super().delete(request,*args,**kwargs)
        
