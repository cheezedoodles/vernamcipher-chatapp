# Generated by Django 4.0.5 on 2022-06-27 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('created',)},
        ),
    ]