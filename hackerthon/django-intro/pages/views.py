from django.shortcuts import render
import random
from datetime import datetime


# Create your views here.
def index(request):  # request : 사용자의 요청
    return render(request, 'index.html')  # index.html 로 이동 + request 전달


def dinner(request):
    menu = ['순대', '국수', '곱창', '피자']
    choice = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': choice})  # dictionary 형태로 전달


def greeting(request, name):
    return render(request, 'greeting.html', {'name': name})


def introduce(request, name, age):
    return render(request, 'introduce.html', {'name': name, 'age': age})


def template_language(request):
    menus = ['짜장면', '짬뽕', '볶음밥', '양장피']
    messages = ['apple', 'banana', 'mango', 'cucumber']
    my_sentence = 'Life is short, you need python'
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'messages': messages,
        'my_sentence': my_sentence,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }

    return render(request, 'template_language.html', context)
