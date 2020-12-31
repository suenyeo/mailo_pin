from django.urls import path

app_name ='profile'

urlpatterns = [
    path('profiles/', include('profileapp.urls')),
]