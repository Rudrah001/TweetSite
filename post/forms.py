from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'bg-gray-900 text-white border border-gray-600 rounded p-3 w-full',
                'placeholder': 'Enter your tweet...',
                'rows': 4
            }),

            'photo': forms.ClearableFileInput(attrs={
                'class': 'bg-gray-900 text-white border border-gray-600 rounded p-2 w-full'
            }),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # style all fields without removing default Django behavior
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 bg-gray-900 border border-gray-600 rounded text-white focus:outline-none focus:border-blue-500'
            })