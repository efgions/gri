from django import forms
from .models import FeedbackMessage


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Имя',
            'email': 'Email',
            'message': 'Сообщение',
        }