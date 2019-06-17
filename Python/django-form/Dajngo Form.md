# Dajngo Form



## django 설치

$ pip install django

$ django-admin startproject django_form .

$ python manage.py runserver

​	http://127.0.0.1:8000/  로 접속해서 홈페이지 뜨는지 확인

$ python manage.py startapp boards



## settings.py 수정

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