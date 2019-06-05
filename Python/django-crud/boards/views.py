from django.shortcuts import render
from .models import Board


# Create your views here.
def index(request):
    return render(request, 'boards/index.html')


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    # new 에서 보낸 데이터를 변수에 담아서 출력!
    title = request.GET.get('title')
    content = request.GET.get('content')
    print(title, content)
    board = Board()
    board.title = title
    board.content = content
    board.save()

    return render(request, 'boards/create.html')

