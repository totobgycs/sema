from google.cloud import translate

from demo.models import *

def get_translated_message (message, target_languge):

    # Instantiates a client
    translate_client = translate.Client()

    # Translate text
    try:
        translation = translate_client.translate(
            message.text_native,
            source_language=message.lang_native.lang_iso,
            target_language=target_languge.lang_iso)['translatedText']
    except:
        translation = 'Transaltion error.'
    
    return translation

