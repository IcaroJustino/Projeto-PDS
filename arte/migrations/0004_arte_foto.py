# Generated by Django 3.2.3 on 2021-08-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0003_auto_20210814_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]