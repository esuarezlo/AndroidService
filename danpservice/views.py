from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'danpservice/index.html')


def addtoken(request):
    if request.method == 'POST':
        userid = request.POST["userid"]
        token = request.POST["token"]
        dict = {
            'userid': userid,
            'token': token
        }

    elif request.method == 'GET':
        token = "get method, no token"

    return HttpResponse(token)


def sendmessage(request):
    if request.method == 'POST':
        message = request.POST["message"]
        token = request.POST["token"]
        dict = {
            'message': message,
            'token': token
        }
    else:
        dict = {
            'message': "message",
            'token': "token"
        }

        return JsonResponse(dict, safe=False)
