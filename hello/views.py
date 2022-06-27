from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'hello/index.html')


def addtoken(request):
    if request.method == 'POST':
        userid = request.POST["userid"]
        token = request.POST["token"]
        dict = {
            'userid': userid,
            'password': token
        }

        return JsonResponse(dict, safe=False)


def users(request):
    dict = {
        'userid': 'userid',
        'password': 'token'
    }

    return JsonResponse(dict)
