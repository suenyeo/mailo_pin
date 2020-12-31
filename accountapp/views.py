from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .models import Helloworld

# Create your views here.
from .templates.accountapp.forms import AccountUpdateForm


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            temp = request.POST.get("hello_world_input")
            new_hello_world = Helloworld()
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list = Helloworld.objects.all()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            hello_world_list = Helloworld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'context': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/create.html"

class AccountDetailView(LoginRequiredMixin, DetailView):
    login_url =reverse_lazy('accountapp:login')

    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    login_url =reverse_lazy('accountapp:login')

    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/update.html"

class AccountDeleteView(DeleteView):

    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = "accountapp/delete.html"

    # LoginRequiredMixin을 사용하지 않는 경우 GET/POST 함수를 상속하여 유저권한 확인 추가하는 방법
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else: 
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()