# Generated by Django 2.1.3 on 2018-11-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='auth',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
