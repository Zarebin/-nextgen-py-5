from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ShortUrl, Profile


class CreateNewShortUrl(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }

class SignUpForm(UserCreationForm):
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=11)
    class Meta:
        model = User
        fields = ('username', 'country','phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.create(user=user, country=self.data['country'], phone_number= self.data['phone_number'])
        return user
