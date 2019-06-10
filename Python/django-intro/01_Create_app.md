# Django - Create app



## app 생성

$ python manage.py startapp `app이름`

![1559644885595](assets/1559644885595.png)

- admin.py   : 관리자페이지를 커스텀할 수 있다
- apps.py     : app의 정보가 담긴다.
- models.py  : 모델들을 정의한다.
- tests.py      : 테스트코드를 작성해 테스트할 수 있다.
- views.py     : 특정 html로 이동시켜준다. (flask의 @app.route,  spring의 controller 역할)



## app 등록

![1559644960129](assets/1559644960129.png)

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





