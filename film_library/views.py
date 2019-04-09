from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import User, Film
from .forms import UserForm, FilmForm
from django.utils import timezone


def users_list(request):
    users = User.objects.all()
    return render(request, 'film_library/users_list.html', {'users': users})


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_date = timezone.now()
            user.save()
            return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'film_library/user_new.html', {'form': form})


def films_list(request, pk):
    user = get_object_or_404(User, pk=pk)
    films = Film.objects.filter(user=user)
    return render(request, 'film_library/films_list.html', {'films': films, 'user': user})


def film_new(request, user_pk):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save(commit=False)
            film.added_date = timezone.now()
            user = get_object_or_404(User, pk=user_pk)
            film.user = user
            film.save()
            return redirect('films_list', pk=user_pk)
    else:
        form = FilmForm()
    return render(request, 'film_library/film_edit.html', {'form': form})
