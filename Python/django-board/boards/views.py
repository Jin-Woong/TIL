from django.shortcuts import render
from .models import Board


def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet type
    boards = Board.objects.all()
    context = {'boards': boards}  # html 에 넘겨주기 위한 dictionary type
    return render(request, 'boards/index.html', context)  # index 함수가 실행되면 index.html 로 이동


# 사용자 입력을 받는 페이지 렌더링
def new(request):
    return render(request, 'boards/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    print(title, content)
    board = Board(title=title, content=content)
    board.save()
    return render(request, 'boards/create.html')
