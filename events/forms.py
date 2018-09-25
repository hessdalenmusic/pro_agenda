form django import forms
from .models import Event, Comments

class EventForm(forms.modelForm):
    """Formulário utilizado para criação de novos eventos"""
    class Meta:
        model = Event
        fields = ['date', 'event', 'priority']

class CommentForm(forms.ModelForm):
    """formulário utilizando para craiação de comentarios"""
    class Meta:
        model = Comment
        fields = ['text', 'author', 'email', 'event']