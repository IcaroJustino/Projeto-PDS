# Generated by Django 3.2.3 on 2021-09-02 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0019_auto_20210901_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='formato',
            field=models.CharField(choices=[('JPEG', 'JPEG'), ('JPG', 'JPG'), ('SVG', 'SVG'), ('PNG', 'PNG'), ('BPM', 'BPM'), ('TIFF', 'TIFF'), ('GIF', 'GIF'), ('EPS', 'EPS')], default='Sem detalhes', max_length=4),
        ),
    ]
