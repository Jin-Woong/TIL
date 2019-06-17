from django.shortcuts import render, redirect, get_object_or_404
from .models import Board


def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards, }
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'boards/create.html')

    else:  # request.method == 'POST't
        # Board 정보를 받아서 데이터베이스에 제공하는 로직

        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:index')


# boards/3/
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
