from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'user_id',
        )
