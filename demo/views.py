from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from demo.models import *

def mock1(request):
  return render(
    request,
    'demo/mock1.html',
    {})

def index(request):

  
  languages = Language.objects.all()[:10]
  dlanguages = [lang.lang_native + ' (' + lang.lang_english + ')' for lang in languages]

  messages = Message.objects.all()

  dmessages = []
  for message in messages:
    dmessage = {}
    dmessage['timestamp'] = message.timestamp
    dmessage['translated_text'] = message.text_native
    dmessage['note'] = "Raw data"
    dmessages.append(dmessage) 
  return render(
    request,
    'demo/index.html',
    {
      'messages': dmessages,
      'languages': dlanguages
    })

