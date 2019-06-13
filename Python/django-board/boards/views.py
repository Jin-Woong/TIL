from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Board, Comment


@require_GET  # GET 요청에만 동작하도록 설정
def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet type
    boards = Board.objects.all()
    context = {'boards': boards}  # html 에 넘겨주기 위한 dictionary type
    return render(request, 'boards/index.html', context)  # index 함수가 실행되면 index.html 로 이동


# 사용자 입력을 받는 페이지 렌더링
@require_http_methods(['GET', 'POST'])
def new(request):
    # GET
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    # POST
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.id)


# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     print(request.POST)
#     print(title, content)
#     board = Board(title=title, content=content)
#     board.save()
#     return redirect(f'/boards/{board.id}')
# get 요청은 작업이 끝나면 render 로 처리,
# post 요청은 작업이 긑나면 redirect 로 처리한다.


# 특정 게시글 하나만 가져온다.
def detail(request, board_id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를 출력
    board = get_object_or_404(Board, id=board_id)
    comments = board.comment_set.order_by('-id').all()
    context = {'board': board,
               'comments': comments}
    return render(request, 'boards/detail.html', context)


# 특정 게시글 하나만 삭제한다.
@require_http_methods(['POST'])
def delete(request, board_id):
    # if request.method == 'GET':
    #     # GET 요청으로 들어오면 detail page 로 다시 redirect
    #     return redirect('boards:detail', id)
    # else:
    #     # POST 요청으로 들어오면 정상 삭제
    # board = Board.objects.get(id=id)
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('boards:index')  # 삭제 후 리스트가 나오는 index 페이지로 이동


# 게시글 수정 페이지 렌더링
def edit(request, board_id):
    # 1. 사용자의 요청이 GET 인지 POST 인지 확인한다.
    # board = Board.objects.get(id=id)  # Dont Repeat Yourself
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'GET':
        # 2. GET 요청이면 사용자에게 수정할 페이지를 보여준다.
        context = {'board': board}
        return render(request, 'boards/edit.html', context)
    else:
        # 3. POST 요청이면 사용자가 보낸 데이터를 받아서 수정한 뒤
        # detail page 로 redirect 한다.
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        # 수정로직
        board.title = title
        board.content = content
        board.image = image
        board.save()
        return redirect('boards:detail', board_id)

    # def update(request, id):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content 에 맞게
    #     # 수정한 뒤 저장하는 로직
    #     # 1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
    #     board = Board.objects.get(id=id)
    #     # 2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
    #     board.title = title
    #     board.content = content
    #     # 3. 저장한다.
    #     board.save()
    #     return redirect('boards:detail', id)


def comment_create(request, board_id):
    # 댓글 생성하는 로직
    content = request.POST.get('content')
    comment = Comment()
    comment.content = content
    comment.board_id = board_id
    comment.save()
    print(comment)
    return redirect('boards:detail', board_id)


@require_POST  # POST 요청에만 동작하도록 설정
def comment_delete(request, board_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('boards:detail', board_id)
