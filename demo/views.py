from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def mock1(request):
    return render(
      request,
      'demo/mock1.html',
      {})

def index(request):
    return render(
      request,
      'demo/index.html',
      {'greeting': 'Proof of concept for a multi lingual chat app. For SEMA.'})

