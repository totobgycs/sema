# Generated by Django 2.2.4 on 2019-09-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='lang_iso',
            field=models.CharField(default='en', max_length=2, unique=True),
        ),
    ]
