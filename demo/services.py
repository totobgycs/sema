from google.cloud import translate

from demo.models import *

def get_translated_message (message, target_language):

    if message.lang_native.lang_iso == target_language.lang_iso:
        return message.text_native

    translation, _ = Translation.objects.get_or_create(
        message = message,
        lang_target = target_language,
        defaults = {'text_translated': lambda : get_google_translation(
            source_language = message.lang_native.lang_iso,
            target_language = target_language.lang_iso,
            text = message.text_native
        )})
   
    return translation.text_translated

def get_google_translation(source_language, target_language, text):

    if source_language == target_language:
        return text

    # Instantiates a client
    translate_client = translate.Client()

    # Translate text
    try:
        translation = translate_client.translate(
            text,
            source_language=source_language,
            target_language=target_language)['translatedText']
    except:
        translation = 'Transaltion error from {} to {}.'.format(source_language, target_language)
    
    return translation
