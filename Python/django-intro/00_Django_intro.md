# Django_intro



## 설치

$  pip django install



## 프로젝트 시작

$ django-admin startproject `프로젝트명` `디렉토리`

​	ex) $ django-admin startproject intro .

​		django 프로젝트를 현재 디렉토리(.)에서 intro라는 이름으로 시작



## 프로젝트 파일

![1559644054119](assets/1559644054119.png)



- ` __init__.py`  : 하나의 python 패키지로 다루겠다
- `settings.py`  : 프로젝트 설정들이 담긴 파일
- `urls.py` 		: 요청받은 url을 특정함수에 매핑해주는 역할 
- `wsgi.py` 		: 나중에 배포를 할때 사용될 파일 
- `db.sqlite3`    : django의 기본 데이이스 



## Django 실행

$ python manage.py runserver

```
Watching for file changes with StatReloader
Performing system checks...
...
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

​	위와 비슷하게 출력되고 http://127.0.0.1:8000/를 클릭하거나 웹브라우저에서 http://127.0.0.1:8000/로 접속

![1559644073807](assets/1559644073807.png)







