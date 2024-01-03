from django import forms
from document.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'attachment']
        
