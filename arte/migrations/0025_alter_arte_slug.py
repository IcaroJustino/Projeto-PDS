# Generated by Django 3.2.3 on 2021-09-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0024_alter_arte_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
