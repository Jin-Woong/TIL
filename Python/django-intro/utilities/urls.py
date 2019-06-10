from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index)  # settings.py 에 pages 를 먼저 등록해 pages 내의 index.html을 불러온 것
]