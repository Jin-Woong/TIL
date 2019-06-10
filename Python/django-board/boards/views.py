from django.shortcuts import render, redirect
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
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(request.POST)
    print(title, content)
    board = Board(title=title, content=content)
    board.save()
    return redirect(f'/boards/{board.id}')
    # get 요청은 작업이 끝나면 render 로 처리,
    # post 요청은 작업이 긑나면 redirect 로 처리한다.


# 특정 게시글 하나만 가져온다.
def detail(request, id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를 출력
    board = Board.objects.get(id=id)

    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)


# 특정 게시글 하나만 삭제한다.
def delete(requests, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards/')  # 삭제 후 리스트가 나오는 index 페이지로 이동
