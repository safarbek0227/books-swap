from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder':'Repeat password'}))

    class Meta:
        model = User
        fields = ('name', 'surname', 'username', 'age', 'phone', 'gender', 'address')
        widgets = {
            "username":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Username', 'autocomplete':"off"}),
            "name":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Name', 'autocomplete':"off"}),
            "surname":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Sourname', 'autocomplete':"off"}),
            'age': forms.TextInput(attrs={'class': 'unique d-block', 'placeholder': 'Age', 'autocomplete':"off"}),
            'phone': forms.TextInput(attrs={'pattern': r'[0-9]{2}-[0-9]{3}-[0-9]{2}-[0-9]{2}', 'placeholder': 'XX-XXX-XX-XX', 'class': '' , 'autocomplete':"off"})
        }



    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']




