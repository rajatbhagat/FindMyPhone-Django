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
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print('Success')
                return render(request, 'website/googlemap.html', {})
            else:
                print('Account blocked')
                return HttpResponse('Account bloacked')
        else:
            return HttpResponse('Invalid details')
    else:
        return HttpResponse('POST not identified')
