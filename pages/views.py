from django.shortcuts import render

from django.views.generic import TemplateView


def about(request):
    return render(request, 'pages/about.html')

def index(request):
    return render(request, 'pages/index.html')