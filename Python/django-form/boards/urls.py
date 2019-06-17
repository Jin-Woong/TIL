from . import views
from django.urls import path

# 경로 맵 이름 지정 'boards:detail
app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_pk>/', views.detail, name='detail'),  # ex) boards/3/
    path('create/', views.create, name='create'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
]
