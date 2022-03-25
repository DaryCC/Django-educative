from django import forms

class SearchForm (forms.Form):
    q = forms.CharField()

class TestForm (forms.Form):
    text = forms.CharField(initial="eje",min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=0)
    email = forms.EmailField(initial="correo")

