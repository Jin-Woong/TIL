# Dajngo Form



## django 설치

$ pip install django

$ django-admin startproject django_form .

$ python manage.py runserver

​	http://127.0.0.1:8000/  로 접속해서 홈페이지 뜨는지 확인

$ python manage.py startapp boards



## django_form/settings.py 수정

```python
#...
INSTALLED_APPS = [
    # local apps
    'boards',

    # django apps
    #...
]
#...
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
#...
```



## .gitignore 생성

<https://www.gitignore.io/>

![1560732000359](assets/1560732000359.png)



## boards/models.py 수정

```python
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=20)  # input
    content = models.TextField()  # textarea
    createed_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
```

 - 모델 생성 후 migration

   $ python manage.py makemigrations

   $ python manage.py migrate



## boards/admin.py 수정

```python
from django.contrib import admin
from .models import Board


@admin.register(Board)  # Board 를 이용한 페이지?
class BoardAdmin(admin.ModelAdmin):  # admin.ModelAdmin 을 상속받는다.
    list_display = ('title', 'content', 'created_at', 'updated_at',)  # 목록에서 보여줄 필드 설정
    readonly_fields = ['created_at', 'updated_at', ]  # 읽기전용 필드를 볼 수 있도록 추가
```

​	<http://127.0.0.1:8000/admin/>

![1560735306039](assets/1560735306039.png)

![1560735385122](assets/1560735385122.png)

​	- BOARD 추가 버튼을 눌러 데이터를 입력할 수 있다.

## index page URL 경로 작성

### django_form/urls.py 수정

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
```

	- boards/ 로 들어오는 url들을  boards.urls에서 처리하도록 넘겨준다.



### boards/urls.py 생성

```python
from . import views
from django.urls import path

# 경로 맵 이름 지정 'boards:detail
app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
]
```



### boards/views.py 수정

```python
from django.shortcuts import render
from .models import Board

def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards, }
    return render(request, 'boards/index.html', context)
```







## django bootstrap

$ pip install django-bootstrap4



### django-form/setting  수정

```python
INSTALLED_APPS = [
	#...

    # 3rd party apps
    'bootstrap4',
    
    #...
]   
```



### boards/base.html 수정

```html
{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    {% bootstrap_css %}
</head>
<body>
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
    {% bootstrap_javascript jquery='full' %}
    <!-- 자바스크립트 -->
</body>
</html>
```



### boards/form.html 수정

```html
{% extends 'boards/base.html' %}
{% load bootstrap4 %}


<!-- GET /boards/create/ -->
{% block body %}
    {% if request.resolver_match.url_name == 'create' %}
    <h1>새로운 게시글 작성</h1>
    {% else %} <!-- update 가 들어오면 -->
    <h1>게시글 수정</h1>
    {% endif %}

    <!-- POST /boards/create/ -->
    <form action="" method="post">  <!-- 동일한 url 로 보낼 경우 action 생략 가능 -->
                                    <!-- create 는 create 로, update 는 update 로 처리 -->
        {% csrf_token %}
        {% bootstrap_form form layout='horizontal' %}  <!-- bootstrap_form 을 form 에 적용 -->
        {% buttons submit="Submit" reset="Cancel" %}
        {% endbuttons %}
    </form>

    {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'boards:index' %}">[뒤로가기]</a>
    {% else %}
    <a href="{% url 'boards:detail' board_pk %}">[뒤로가기]</a>
    {% endif %}

{% endblock %}
```



