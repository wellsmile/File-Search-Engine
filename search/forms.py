#coding=utf-8
'''
Created on 2017��10��30��

@author: user
'''
from django import forms

class SearchForm(forms.Form):
    file_title = forms.CharField(required=False, 
                               widget=forms.TextInput(attrs={'id': 'file_title', 'placeholder': 'any word', 'class': 'form-control'}))
    file_content = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_content', 'placeholder': 'any word', 'class': 'form-control'}))
    file_name = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_name', 'placeholder': 'any word', 'class': 'form-control'}))
    file_author = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={'id': 'file_author', 'placeholder': 'any word', 'class': 'form-control'}))
