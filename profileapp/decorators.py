from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def Profile_ownership_requried(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(id = kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated