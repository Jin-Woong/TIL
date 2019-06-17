from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .models import Board
from .forms import BoardForm


@require_GET
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards, }
    return render(request, 'boards/index.html', context)


@require_http_methods(['GET', 'POST'])
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
    return render(request, 'boards/form.html', context)


# boards/3/
@require_GET
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)


# delete 요청을 POST 요청으로만
@require_POST
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    board.delete()
    return redirect('boards:index')


@require_http_methods(['GET', 'POST'])
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    # POST boards/3/update
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            board.save()
            return redirect('boards:detail', board.pk)

    # GET boards/3/update
    else:
        form = BoardForm(initial=board.__dict__)  # board 데이터 할당

    # GET 요청 또는 유효하지 않는 값일 때
    context = {'form': form}
    return render(request, 'boards/form.html', context)  # form 내에 데이터가 있는 상태로 보인다.
