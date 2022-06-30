from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import sqlite3

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
        # con = sqlite3.connect('example.db')
        # cur = con.cursor()
        #
        # # Create table
        # cur.execute('''CREATE TABLE tokens (token text)''')
        # con.commit()

    elif request.method == 'GET':
        dict ={ "get method":" no token"}

    return JsonResponse(dict, safe=False)


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
