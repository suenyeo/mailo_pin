from django.http import HttpResponse
from django.shortcuts import render
from .models import Helloworld

# Create your views here.
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("hello_world_input")
        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'context': new_hello_world})

    else:
        return render(request, 'accountapp/hello_world.html', context={'context': 'GET SUC!!'})
