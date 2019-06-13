from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class Board(models.Model):
    title = models.CharField(max_length=20)  # CharField 는 반드시 max_length 지정
    content = models.TextField()  # textarea 와 연동 가능
    # image = models.ImageField(blank=True)  # 해당 필드에 아무것도 안들어가도 된다 -> null 가능
    image = ProcessedImageField(
        upload_to='boards/images',  # 저장 위치(media 이후의 경로)
        processors=[Thumbnail(200, 300)],  # 썸네일
        format='JPEG',
        options={'quality': 60},  # field 이후 () 내의 값 변경은 migrate 안해도 반영된다.g
    )
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
