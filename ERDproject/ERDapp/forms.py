from django import forms

from .models import Task


#class TaskForm(forms.Form):
    #title = forms.CharField(max_length=100, label="Название задачи")
    #description = forms.CharField(widget=forms.Textarea, label = "описание задачи", required=False)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

