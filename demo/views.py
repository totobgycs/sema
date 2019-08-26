from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def mock1(request):
    return render(
      request,
      'demo/mock1.html',
      {})

def index(request):
    messages = [
      {
        'timestamp':'19:58',
        'translated_text':'SEMA is the Global Network of Victims and Survivors to End Wartime Sexual Violence.',
        'note':'originally posted in English'
       },
      {
        'timestamp':'20:10',
        'translated_text':'SEMA literally means “Speak Out” in Swahili.',
        'note': 'originally posted in English'
      },
      {
        'timestamp':'20:12',
        'translated_text':'There are survivors of wartime rape from 21 countries in Africa, South America, the Middle East, and Europe represented in the SEMA network.',
        'note':'originally posted in English'
        },
      ]
    return render(
      request,
      'demo/index.html',
      {'messages': messages})

