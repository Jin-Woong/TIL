from . import views
from django.urls import path

# 경로 맵 이름 지정 'boards:detail
app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_pk>/', views.detail, name='detail'),  # ex) boards/3/
    path('create/', views.create, name='create'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/update/', views.update, name='update'),

    # Comments
    # POST /boards/3/comments
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

    # like
    path('<int:board_pk>/like/', views.like, name='like'),
]
