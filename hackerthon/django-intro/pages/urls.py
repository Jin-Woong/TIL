from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),

    path('artii/', views.artii),
    path('result/', views.result),

    path('catch/', views.catch),
    path('throw/', views.throw),

    path('isitbirthday/', views.isitbirthday),

    path('template_language/', views.template_language),

    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('greeting/<str:name>/', views.greeting),
    path('dinner/', views.dinner),
    path('index/', views.index),  # index/ 를 views.index 로 매핑   '/' 로 끝나야 한다
]
