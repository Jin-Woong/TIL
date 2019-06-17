from django.contrib import admin
from .models import Board


@admin.register(Board)  # Board 를 이용한 페이지?
class BoardAdmin(admin.ModelAdmin):  # admin.ModelAdmin 을 상속받는다.
    list_display = ('title', 'content', 'created_at', 'updated_at',)  # 목록에서 보여줄 필드 설정
    readonly_fields = ['created_at', 'updated_at', ]  # 읽기전용 필드를 볼 수 있도록 추가


