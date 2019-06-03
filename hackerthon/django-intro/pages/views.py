from django.shortcuts import render
import random


# Create your views here.
def index(request):  # request : 사용자의 요청
    return render(request, 'index.html')  # index.html 로 이동 + request 전달


def dinner(request):
    menu = ['순대', '국수', '곱창', '피자']
    choice = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': choice})  # dictionary 형태로 전달


def greeting(request, name):
    return render(request, 'greeting.html', {'name': name})
