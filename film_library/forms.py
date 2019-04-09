from django import forms
from .models import User, Film


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login',)


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('original_title', 'production', 'country', 'year',)
