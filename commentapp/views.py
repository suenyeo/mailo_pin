from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_requried
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_commend = form.save(commit=False)
        temp_commend.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_commend.writer = self.request.user
        temp_commend.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_requried, 'get')
@method_decorator(comment_ownership_requried, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse ('articleapp:detail', kwargs={'pk':self.object.article.pk})