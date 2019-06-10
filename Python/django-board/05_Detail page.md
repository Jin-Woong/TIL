## Detail page 생성

boards/urls.py 수정

```python
urlpatterns = [
    path('', views.index),  # .../boards/ -> views.index 실행
    path('new/', views.new),  # 사용자의 입력을 받아서 게시글을 작성하는 곳
    path('create/', views.create),  # 사용자가 입력한 데이터를 전송받고 실제 DB에 작성 및 피드백
    path('<int:id>/', views.detail),  # .../boards/<id>/
]
```



boards/views.py 수정

```python
# ...

# 특정 게시글 하나만 가져온다.
def detail(request, id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 content 를 출력
    board = Board.objects.get(id=id)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)

```



boards/templates/boards/detail.html 생성

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1>Detail page</h1>
    <p>{{board.id}}번째 글</p>
    <p>{{board.created_at}}</p>
    <p>내용 : {{board.content}}</p>
    <hr/>
    <a href="/boards/">Back</a>
{% endblock %}
```



index page => detail page 연결

boards/templates/boards/index.html 수정

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1>Welcome to boards</h1>
    <hr/>
    {% for board in boards %}
        <p>글 번호 : {{board.id}} </p>
        <p>글 제목 : {{board.title}}</p>
        <a href="/boards/{{board.id}}">[세부내용]</a>
        <hr/>
    {% endfor %}
    <a href="/boards/new/">새로운 글 작성하러 가기</a>
{% endblock %}
```

 - `<a href="/boards/{{board.id}}">세부내용</a>` 추가
 - 리스트 가독성을 위해 <p>글 내용</p> 라인 삭제



새로운 글 작성 시 세부내용 페이지로 이동

boards/templates/boards/views.py 수정

```python
# ...
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(request.POST)
    print(title, content)
    board = Board(title=title, content=content)
    board.save()
    return redirect(f'/boards/{board.id}')
# ...
```

	-  `return redirect(f'/boards/{board.id}')` 수정

