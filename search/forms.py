#coding=utf-8
'''
Created on 2017��10��30��

@author: user
'''
from django import forms

class SearchForm(forms.Form):
    file_title = forms.CharField(required=False, 
                               widget=forms.TextInput(attrs={'id': 'file_title', 'placeholder': 'please enter the keyword which you want to search', 'class': 'form-control'}))
    file_content = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_content', 'placeholder': 'please enter the keyword which you want to search', 'class': 'form-control'}))
    file_name = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_name', 'placeholder': 'please enter the keyword which you want to search', 'class': 'form-control'}))
    file_author = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_author', 'placeholder': 'please enter the keyword which you want to search', 'class': 'form-control'}))
