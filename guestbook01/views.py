from django.shortcuts import render
from django.http import HttpResponseRedirect

from guestbook01 import models


def index(request):
    results = models.findall()
    data = { "guestbook_list": results }
    return render(request, 'guestbook01/index.html', data)


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    models.insert(name, password, message)

    return HttpResponseRedirect("/guestbook01")


def deleteform(request):
    return render(request, 'guestbook01/deleteform.html')


def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    models.deleteby_no_and_password(no, password)

    return HttpResponseRedirect("/guestbook01")


