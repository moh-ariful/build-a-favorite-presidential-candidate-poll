# Generated by Django 3.2.9 on 2022-10-11 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]