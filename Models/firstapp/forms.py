from django import forms

class SearchForm (forms.Form):
    q = forms.CharField()

class TestForm (forms.Form):
    text = forms.CharField(initial="eje",min_length=7)
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=0)
    email = forms.EmailField(initial="correo")

    def clean_integer(self):
        # self.is_valid()
        # integer= self.cleaned_data.get("integer")
        integer= self.cleaned_data["integer"]
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer
