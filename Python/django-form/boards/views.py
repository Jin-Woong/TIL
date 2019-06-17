from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm


def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards, }
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'POST':
        # Board 정보를 받아서 데이터베이스에 제공하는 로직
        form = BoardForm(request.POST)
        if form.is_valid():  # 유효성 검사
            title = form.cleaned_data.get('title')  # cleaned_data : 값을 깔끔하게 다듬어서 꺼내는 요청
            content = form.cleaned_data.get('content')
            board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)
    else:  # GET 요청 또는 유효성 검사를 충족하지 못한 경우
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/create.html', context)


# boards/3/
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
