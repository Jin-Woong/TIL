## POST 방식으로 변경

boards/templates/boards/new.html 수정

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1>New page</h1>
    <form action="/boards/create/" method="post">
        {% csrf_token %}
        <!-- for="id" -> 해당 태그의 id를 찾는다 -->
        <!-- name : 데이터가 담겨 전송되는 이름 변수명과 비슷-->
        <label for="title">Title</label><br/>
        <input name="title" id="title" type="text"/><br/>

        <label for="content">Content</label><br/>
        <textarea name="content" id="content"></textarea><br/>
        <!--textarea#content 를 입력하고 tab 을 누르면 id가 content 인 textarea 생성-->

        <input type="submit" />
    </form>
    <a href="/boards/">Back</a>
{% endblock %}
```

method="post", {% csrf_token %} 추가



boards/views.py 수정

```python
from django.shortcuts import render, redirect

...

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(request.POST)
    print(title, content)
    board = Board(title=title, content=content)
    board.save()
    return redirect('/boards/')
	# get 요청은 작업이 끝나면 render 로 처리,
    # post 요청은 작업이 긑나면 redirect 로 처리한다.

```

