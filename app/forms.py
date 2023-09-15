from django import forms 
from . models import Category
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    category =forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label = 'Select category'
    )
    start_datetime = forms.DateTimeField()
    end_datetime = forms.DateTimeField()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']