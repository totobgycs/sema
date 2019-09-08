from django.db import models

class Language(models.Model):
    # the language name in the original language, e.g. 'Magyar'
    lang_native = models.CharField(max_length=30, unique=True)
    # the language name in English, e.g. 'Hungarian'
    lang_english = models.CharField(max_length=30, unique=True)
    # ISO 639-1 code of teh language
    lang_iso = models.CharField(max_length=2, unique=True, default='en')
    
    def __str__(self):
        return 'Language: '+self.lang_english


class Message(models.Model):
    timestamp = models.DateTimeField()
    text_native = models.CharField(max_length=200)
    lang_native = models.ForeignKey(Language, on_delete=models.PROTECT)
    
    def __str__(self):
        return 'Message: '+self.text_native[0:40]+'...'


class Translation(models.Model):
    message = models.ForeignKey(Message, on_delete=models.PROTECT)
    lang_target = models.ForeignKey(Language, on_delete=models.PROTECT)
