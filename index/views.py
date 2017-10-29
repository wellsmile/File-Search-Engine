from django.shortcuts import render

# Create your views here.


def index(request, template):
    return render(request, template)