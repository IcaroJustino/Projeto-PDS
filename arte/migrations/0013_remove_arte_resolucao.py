# Generated by Django 3.2.3 on 2021-08-26 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0012_alter_tags_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arte',
            name='resolucao',
        ),
    ]
