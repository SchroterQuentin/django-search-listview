from django import forms

class PageForm(forms.Form):
    page = forms.IntegerField(
        widget=forms.HiddenInput()
    )
