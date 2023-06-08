from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm, TestForm

def index(request):
    return render(request,'Models/index.html')

def home(request):
    return HttpResponse("Welcome to home page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")

def searchform(request):
    forms = SearchForm()

    initial_dict= {
            "text": "Some initial data",
            "integer": 123,
        }

    # test_form = TestForm()

    form = TestForm(request.POST or None, initial=initial_dict)
    data = "None"
    text = "None"

    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
        print("puta madre no se que está pasando.")
    return render(request, 'Models/formulario.html', {"primer_formulario": form, "data": data, "text": text})

