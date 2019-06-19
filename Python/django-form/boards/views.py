from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Board, Comment
from .forms import BoardForm, CommentForm


@require_GET
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards, }
    return render(request, 'boards/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # Board 정보를 받아서 데이터베이스에 제공하는 로직
        form = BoardForm(request.POST)
        if form.is_valid():  # 유효성 검사
            # title = form.cleaned_data.get('title')  # cleaned_data : 값을 깔끔하게 다듬어서 꺼내는 요청
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            board = form.save(commit=False)
            board.user = request.user
            board = form.save()
            return redirect('boards:detail', board.pk)
    else:  # GET 요청 또는 유효성 검사를 충족하지 못한 경우
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/form.html', context)


# boards/3/
@require_GET
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comments = board.comment_set.order_by('-pk')
    comment_form  = CommentForm()
    context = {
        'board': board,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)


# delete 요청을 POST 요청으로만
@require_POST
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.user != board.user:
        return redirect('boards:detail', board_pk)
    board.delete()
    return redirect('boards:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    # POST boards/3/update
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            # board.title = form.cleaned_data.get('title')
            # board.content = form.cleaned_data.get('content')
            # board.save()
            board = form.save(commit=False)
            board.user = request.user
            board = form.save()  # instance=board -> Board 를 새로 생성하지않고 기존의 Board 를 업데이트
            return redirect('boards:detail', board.pk)

    # GET boards/3/update
    else:
        form = BoardForm(initial=board.__dict__)  # board 데이터 할당

    # GET 요청 또는 유효하지 않는 값일 때
    context = {
        'form': form,
        'board_pk': board_pk,
    }
    return render(request, 'boards/form.html', context)  # form 내에 데이터가 있는 상태로 보인다.


@require_POST
def comments_create(request, board_pk):
    # 로그인하지 않은 사용자 차단
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    # 댓글 작성 로직
    comment_form = CommentForm(request.POST)  # model form 에 사용자 입력을 받는다.
    # 유효성 검사
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
    # 유저 정보 할당
        comment.user = request.user
        # 같은 말 comment.user_id = request.user.id
    # board 정보 할당
        comment.board_id = board_pk  # pk 로 할당
    # 저장
        comment.save()

    return redirect('boards:detail', board_pk)


def comments_delete(request, board_pk, comment_pk):
    # 댓글 삭제 로직
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('boards:detail', board_pk)
