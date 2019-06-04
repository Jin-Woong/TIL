from django.shortcuts import render
import random
from datetime import datetime
import requests


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


def isitbirthday(request):
    return render(request, 'isitbirthday.html')


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'catch.html', context)


def artii(request):
    return render(request, 'artii.html')


def result(request):
    # 1. form 태그로 날린 데이터를 받는다.
    text = request.GET.get('word')  # name 이 word 인 input 을 받아온다
    # 2. ARTII API 로 요청을 보내고 응답결과를 text 로 fonts 에 저장한다. (fonts 를 받는다.)
    api_url = 'http://artii.herokuapp.com'
    fonts = requests.get(f'{api_url}/fonts_list').text  # artii 페이지에서 fonts_list 를 받아온다

    # 3. fonts(str)를 font_list(list) 으로 바꾼다.
    font_list = fonts.split('\n')

    # 4. random 으로 font 1개를 선택해서 font 라는 변수에 저장한다.
    font = random.choice(font_list)

    # 5. 1번에서 받은 word 와 font 로 다시 요청을 보내서 응답결과를 artii_result 라는 변수에 저장한다.
    artii_result = requests.get(f'{api_url}/make?text={text}&font={font}').text

    # 6. artii_result 에 담긴 문자열을 result.html 로 넘겨준다.
    context ={
        'text': text,
        'font': font,
        'artii_result': artii_result,
    }
    return render(request, 'result.html', context)

