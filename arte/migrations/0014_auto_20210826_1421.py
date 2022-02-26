# Generated by Django 3.2.3 on 2021-08-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0013_remove_arte_resolucao'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='image_height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arte',
            name='image_width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arte',
            name='foto',
            field=models.ImageField(blank=True, height_field='image_width', upload_to='media', width_field='image_height'),
        ),
    ]
