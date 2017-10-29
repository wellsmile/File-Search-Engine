# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import SearchForm

def search(request, template):
    form = SearchForm()
    return render(request, template, {'form': form})
