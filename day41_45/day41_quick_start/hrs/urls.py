#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path
from hrs import views
from django.http import HttpResponse

urlpatterns = [
	path('', views.index, name='index'),
]
