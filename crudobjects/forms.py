from django import forms
from .models import Crudobject, Comment


class CrudobjectForm(forms.ModelForm):


    class Meta:
        model = Crudobject
        fields = ['title', 'crudcover', 'author', 'body', 'status',]


class CrudCommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ['text', 'author', 'crudobject']