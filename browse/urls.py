#coding=utf-8
'''
Created on 2016年10月28日

@author: xiaochengcao
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^browse/$', views.browse, {'template': 'browse/browse.html'}, name='browse'),
]