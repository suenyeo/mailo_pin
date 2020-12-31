from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_requried
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm

class ArticleListView(ListView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/list.html'
    paginate_by = 5

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    form_class = CommentCreationForm

@method_decorator(article_ownership_requried, 'get')
@method_decorator(article_ownership_requried, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


@method_decorator(article_ownership_requried, 'get')
@method_decorator(article_ownership_requried, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:list')

