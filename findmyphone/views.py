from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
import requests
import json
from rest_framework.response import Response
from .models import Device


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        registration_id = request.POST.get('token')
        user = authenticate(username=username, password=password)
        if user:
            device = Device(user=user, registration_id=registration_id)
            device.save()
            return Response('login successful', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('login unsuccessful', status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def make_post_request(data):
    url = 'http://fcm.googleapis.com/fcm/send'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'key=AIzaSyD6OB2ifrTrO4oMTUhJZwv7eexR39tFY0A'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)


def make_phone_ring(request):
    print("hello")
    data = {'to':'fTjnANJx_24:APA91bFU2wa4xYKFExJ16Ou3ekolLbuBTtTkxXFj6iVDamSasSBWkfLMhES7uNMVoXWih3V_kFZ3QKbm9aWQPAf3hA2HYUWUxItSZBKn8enZgsXeTDtnte90Kja-j1mlkLsi82CVvsnb',
            'data':{'message':'Press the button at the bottom to locate the phone.',
                    'ring':'true'}}
    make_post_request(data)
    return HttpResponse("Done")