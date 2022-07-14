from django import forms

category = [
    ('unread', 'Unread'),
    ('checked', 'checked'),
    ('ban', 'Ban'),
]

class choices(forms.Form):
    category = forms.ChoiceField(choices=category,)