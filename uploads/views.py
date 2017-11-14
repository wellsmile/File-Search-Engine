from django.shortcuts import render
from .forms import UploadsForm

# Create your views here.
def uploads(request, template):
    form = UploadsForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
    file_path = cleaned_data['file_path']
    print('##################')
    print(type(file_path))
    if 'uploading' in request.POST.keys():
        print('==============')
        print(type(file_path))
    return render(request, template, {'form': form})