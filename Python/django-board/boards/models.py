from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=20)  # CharField 는 반드시 max_length 지정
    content = models.TextField()  # textarea 와 연동 가능
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 생성되는 시점?
    updated_at = models.DateTimeField(auto_now=True)  # 데이터의 조작이 가해지는 시점
