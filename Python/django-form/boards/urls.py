from . import views
from django.urls import path
# 경로 맵 이름 지정 'boards:detail
app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
]