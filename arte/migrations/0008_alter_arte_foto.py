# Generated by Django 3.2.3 on 2021-08-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0007_alter_arte_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='foto',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
