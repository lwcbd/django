from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def root_to_index(request):
    return redirect('/index')

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def dm(request):
  template = loader.get_template('dm.html')
  return HttpResponse(template.render())

def options(request):
  template = loader.get_template('options.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

