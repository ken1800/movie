# Generated by Django 2.2.1 on 2019-09-20 17:25

from django.db import migrations, models
import hub.models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_auto_20190920_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='hub',
            name='language',
            field=models.CharField(choices=[('PY', 'Python'), ('JS', 'Java Script'), ('JV', 'Java'), ('KOT', 'Kotlin'), ('PHP', 'PHP'), ('HT', 'Html'), ('R', 'R')], default=hub.models.hub.language_default, max_length=200),
        ),
    ]
