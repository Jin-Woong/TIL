from django.db import models

# Create your models here.
class Board(models.Model):
    # id 는 기본적으로 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)  # auto-incrementing primary key.

    # 클래스 변수 => DB 의 필드를 나타냄
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 객체 생성시의 시간
    updated_at = models.DateTimeField(auto_now=True)  # 업데이트시 시간이 저장된다.

    # 인스턴스 자체를 출력할 때 형식을 지정하는 메서드
    def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'
