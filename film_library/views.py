from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User, Film


def users_list(request):
    users = User.objects.all()
    return render(request, 'film_library/users_list.html', {'users': users})


def films_list(request, pk):
    user = get_object_or_404(User, pk=pk)
    films = Film.objects.filter(user=user)
    return render(request, 'film_library/films_list.html', {'films': films, 'user': user})
