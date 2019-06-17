from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods
from .models import Movie


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    # GET
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title=title, title_origin=title_origin, vote_count=vote_count,
                      open_date=open_date, genre=genre, score=score, poster_url=poster_url,
                      description=description)
        movie.save()
        return redirect('movies:detail', movie.id)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {'movie': movie}
    return render(request, 'detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        context = {'movie': movie}
        return render(request, 'update.html', context)
    else:  # POST
        movie.title = request.POST.get('title')
        movie.title_origin = request.POST.get('title_origin')
        movie.vote_count = request.POST.get('vote_count')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie_id)


def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:index')
