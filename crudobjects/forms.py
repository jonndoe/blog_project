from django import forms
from .models import Crudobject, Comment


class CrudobjectForm(forms.ModelForm):


    class Meta:
        model = Crudobject
        fields = ['title', 'crudcover', 'body', 'status',]
        widgets = {
            'author': forms.HiddenInput(),
        }


class CrudCommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'author': forms.HiddenInput(),
            'crudobject': forms.HiddenInput(),
        }