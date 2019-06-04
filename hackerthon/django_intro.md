# Django



## 설치

$  pip django install



## 프로젝트 시작

$ django-admin startproject `프로젝트명` `디렉토리`

​	ex) $ django-admin startproject intro .

​		django 프로젝트를 현재 디렉토리(.)에서 intro라는 이름으로 시작



## 프로젝트 파일

![1559609520438](assets/1559609520438.png)

- ` __init__.py`  : 하나의 python 패키지로 다루겠다
- `settings.py`  : 프로젝트 설정들이 담긴 파일
- `urls.py` 		: 요청받은 url을 특정함수에 매핑해주는 역할 
- `wsgi.py` 		: 나중에 배포를 할때 사용될 파일 
- `db.sqlite3`    : django의 기본 데이이스 



## app 생성

$ python manage.py startapp `app이름`

![1559616768797](assets/1559616768797.png)

- admin.py   : 관리자페이지를 커스텀할 수 있다
- apps.py     : app의 정보가 담긴다.
- models.py  : 모델들을 정의한다.
- tests.py      : 테스트코드를 작성해 테스트할 수 있다.
- views.py     : 특정 html로 이동시켜준다. (flask의 @app.route,  spring의 controller 역할)



## app 등록

![1559624637076](assets/1559624637076.png)

 - intro/settings.py의 INSTALLED_APPS에 생성한 app을 등록해야 프로젝트에서 인식한다.

   ex) pages라는 이름으로 app을 생성했으면 pages의 apps.py에서 PagesConfig 라는 class를 등록

   ​		'pages.apps.PagesConfig'

- 추가로 settings.py에서 한글 및 표준시간도 설정할 수 있다.

  ```python
  # 한글 설정
  LANGUAGE_CODE = 'ko-kr' 
  # 표준시간 설정
  TIME_ZONE = 'Asia/Seoul'
  ```



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

![Screen Shot 2019-06-03 at 16 03 44](assets/58782318-356ab200-8619-11e9-9110-9862f14ac2b3.png)



