from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from demo.models import *

def mock1(request):
  return render(
    request,
    'demo/mock1.html',
    {})

def index(request):
  return redirect(language, label='English')

def language(request, label):

  try:
    language = Language.objects.get(lang_english=label)
  except Language.DoesNotExist:
    language = Language.objects.get(lang_english='English')

  languages = Language.objects.all()[:10]

  messages = Message.objects.all()[:100]

  dmessages = []
  for message in messages:
    dmessage = {}
    dmessage['timestamp'] = message.timestamp
    dmessage['translated_text'] = message.text_native
    dmessage['note'] = "Original message (translation pending)"
    dmessages.append(dmessage) 
  return render(
    request,
    'demo/index.html',
    {
      'messages': dmessages,
      'languages': languages,
      'chosen_language': language,
    })

