from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def account_ownership_requried(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(id = kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated


def not_authenticated(func):
    def decorated(request, *args, **kwargs):
        if request.user.is_authenticated:
             return redirect('index')
        return func(request, *args, **kwargs)
    return decorated