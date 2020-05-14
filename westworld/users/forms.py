from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=256)
    nickname = forms.CharField(label='Nickame', max_length=256)
    email = forms.EmailField(label='Email', max_length=256)
    age = forms.IntegerField(label='Age', min_value=18)