# Delete

boards/urls.py 수정

```python
urlpatterns = [
    path('', views.index),  # .../boards/ -> views.index 실행
    path('new/', views.new),  # 사용자의 입력을 받아서 게시글을 작성하는 곳
    path('create/', views.create),  # 사용자가 입력한 데이터를 전송받고 실제 DB에 작성 및 피드백
    path('<int:id>/', views.detail),  # .../boards/<id>/
    path('<int:id>/delete/', views.delete),  # .../boards/<id>/delete
]
```

	-  `path('<int:id>/delete/', views.delete)` 추가

boards/views.py 수정

```python
# ...

# 특정 게시글 하나만 삭제한다.
def delete(requests, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards/')  # 삭제 후 리스트가 나오는 index 페이지로 이동
```

​	

boards/templates/boards/detail.html   수정

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1>Detail page</h1>
    <p>{{board.id}}번째 글</p>
    <p>{{board.created_at}}</p>
    <p>내용 : {{board.content}}</p>
    <hr/>
    <a href="/boards/{{board.id}}/delete">Delete</a><br/>
    <a href="/boards/">Back</a>

{% endblock %}
```

 - `<a href="/boards/{{board.id}}/delete">Delete</a><br/>` 추가



## POST방식으로 변경

boards/templates/boards/detail.html   수정

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1>Detail page</h1>
    <p>{{board.id}}번째 글</p>
    <p>{{board.created_at}}</p>
    <p>내용 : {{board.content}}</p>
    <hr/>
    <form action="/boards/{{board.id}}/delete/" method="post">
        {% csrf_token %}
        <input class="btn btn-danger" type="submit" value="삭제하기">
    </form>
    <a href="/boards/">Back</a>

{% endblock %}
```

