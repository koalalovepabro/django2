from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from emaillist01 import models
from emaillist01.models import findall


def index(request):
    results = models.findall()
    data = {"emaillist_list": results}
    return render(request, 'emaillist02/index.html', data)


def form(request):
    return render(request, 'emaillist02/form.html')


def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return HttpResponseRedirect("/emaillist02")