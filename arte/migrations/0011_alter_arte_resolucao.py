# Generated by Django 3.2.3 on 2021-08-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0010_auto_20210826_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='resolucao',
            field=models.CharField(max_length=11, verbose_name='Resolução'),
        ),
    ]
