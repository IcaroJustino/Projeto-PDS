# Generated by Django 3.2.3 on 2021-08-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0014_auto_20210826_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arte',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]