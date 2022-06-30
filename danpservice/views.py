from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import sqlite3
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'danpservice/index.html')


@csrf_exempt
def addtoken(request):
    if request.method == 'POST':
        userid = request.POST["userid"]
        token = request.POST["token"]
        dict = {
            'userid': userid,
            'token': token
        }
        # con = sqlite3.connect('example.db')
        # cur = con.cursor()
        #
        # # Create table
        # cur.execute('''CREATE TABLE tokens (token text)''')
        # con.commit()

    elif request.method == 'GET':
        dict ={ "get method":" no token"}

    #return JsonResponse(dict, safe=False)
    data = request.body
    #print(str(data, 'UTF-8'))
    return HttpResponse(str(data, 'UTF-8'), content_type="application/json")


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
