from django.shortcuts import render

# Create your views here.
def uploads(request, template):
    return render(request, template)