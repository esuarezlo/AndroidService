from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def addtoken(request):
    if request.method == 'POST':
        userid = request.POST["userid"]
        token = request.POST["token"]
        dict = {
            'userid': userid,
            'token': token
        }

        return JsonResponse(dict, safe=False)

def sendmessage(request):
    if request.method == 'POST':
        message = request.POST["message"]
        token = request.POST["token"]
        dict = {
            'message': message,
            'token': token
        }

        return JsonResponse(dict, safe=False)