#coding=utf-8
'''
Created on 2017��10��30��

@author: user
'''
from django import forms

class UploadsForm(forms.Form):
    file_path = forms.FilePathField('/root/aaa.xlsx',required=False,
        widget=forms.FileInput(attrs={'id': 'file_path', 'placeholder': 'please enter the keyword which you want to search', 'class': 'form-control'}))
