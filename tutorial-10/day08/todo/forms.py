from django import forms
from todo.models import TodoTask

class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ['title', 'description', 'status']