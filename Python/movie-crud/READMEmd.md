Movie CRUD



## Django 설치 

$ pip install django



## Django 프로젝트 생성

$ django-admin startproject curd .



## Django app 생성

$ python manage.py startapp movies



## app 식별

crud/settings.py 수정



## Model 생성

movies/models.py 수정



## Migration

$ python manage.py makemigrations

$ python manage.py migrate



## Data Load 

movies 디렉토리 내에 fixtures 디렉토리 생성

movies/fixtures 디렉토리에 movies.json 파일 복사

$ python manage.py loaddata movies.json



## 관리자페이지 

movies/admin.py 수정

```bash
$ python manage.py createsuperuser
Username (leave blank to use 'woong'): admin
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```





