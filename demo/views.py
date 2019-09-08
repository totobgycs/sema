from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from demo.models import *
from demo import services

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
    language, _ = Language.objects.get_or_create(lang_english='English', defaults={'lang_native': 'English', 'lang_iso': 'en'})

  languages = Language.objects.all()[:10]

  messages = Message.objects.all()[:100]

  dmessages = []
  for message in messages:
    dmessage = {}
    dmessage['timestamp'] = message.timestamp
    dmessage['translated_text'] = services.get_translated_message(message, language) 
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

