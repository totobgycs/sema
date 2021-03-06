# Generated by Django 2.2.4 on 2019-09-07 17:16

from django.db import migrations
from iso639 import languages

def get_iso639(apps, schema_editor):
    MyModel = apps.get_model('demo', 'language')
    for row in MyModel.objects.all():
        row.lang_iso = languages.get(name=row.lang_english).part1
        row.save(update_fields=['lang_iso'])

class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_language_lang_iso_default'),
    ]

    operations = [
        migrations.RunPython(get_iso639, reverse_code=migrations.RunPython.noop)
    ]
