from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=20)  # CharField 는 반드시 max_length 지정
    content = models.TextField()  # textarea 와 연동 가능
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 생성되는 시점?
    updated_at = models.DateTimeField(auto_now=True)  # 데이터의 조작이 가해지는 시점

    def __str__(self):
        # 1. 첫번째 포스트
        return f'{self.id}. {self.title}'


class Comment(models.Model):
    content = models.TextField()  # 댓글의 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id} - {self.content})>'
