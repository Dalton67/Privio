from django import forms


class EmailForm(forms.Form):
    user_email = forms.CharField(widget=forms.EmailInput(), label='Email', max_length=100)
