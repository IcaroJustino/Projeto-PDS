# Generated by Django 3.2.3 on 2021-08-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0016_alter_arte_formato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='formato',
            field=models.CharField(choices=[('bpm', 'BPM'), ('tiff', 'TIFF'), ('jpeg', 'JPEG'), ('gif', 'GIF'), ('png', 'PNG'), ('eps', 'EPS'), ('svg', 'SVG'), ('png', 'PNG')], default='Sem detalhes', max_length=4),
        ),
    ]
