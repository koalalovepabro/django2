from django.http import HttpResponse
from django.shortcuts import render

def main(request):  # 렌더로 하기

    return render(request, 'helloworld/main.html')

def hello1(request):
    name = request.GET["name"]
    return HttpResponse(f'<h1>Hello {name}</h1><a href="/">main으로 가기</a>', content_type='text/html; charset=utf-8')


def tags(request):  # 렌더로 하기

    return render(request, 'helloworld/tags.html')


def form(request):
    return render(request,'helloworld/form.html')


def join(request):
    email = request.POST['email']  #reqeust안에 get이라는 딕셔너리를 만들어서 입력받은 값을 저장
    password = request.POST['password']
    gender = request.POST["gender"]
    hobbies = request.POST.getlist("hobbies")
    description = request.POST["desc"]

    print(email, password, gender, hobbies, description)
    return HttpResponse('ok', content_type='text/plain; charset=utf-8')