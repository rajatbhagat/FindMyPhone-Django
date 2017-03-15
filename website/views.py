from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    user_login(request)
    return render(request, 'website/home.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print('Success')
                return render(request, 'website/googlemaps.html', {})
            else:
                print('Account blocked')
                return render(request, 'website/home.html', {})
        else:
            print('Wrong details entered')
            return render(request, 'website/home.html', {})
    else:
        print('POST method not working')
        return render(request, 'website/home.html', {})


def get_location(request):
    return render(request, 'website/googlemaps.html', {})
