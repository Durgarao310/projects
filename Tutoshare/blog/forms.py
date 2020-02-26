from django import forms

from .models import Technology

from .models import Tutorial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#class PostForm(forms.Form):
 #   title = forms.CharField()
  #  description = forms.CharField()
   # image = forms.CharField()



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['title','img']    


class TutModelForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = [ 'url', 'websitename', 'tech', 'type', 'plan', 'audience']
        widgets = {
            'type': forms.RadioSelect(),
            'plan': forms.RadioSelect(),
            'audience': forms.RadioSelect(),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        