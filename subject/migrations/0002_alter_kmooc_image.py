# Generated by Django 3.2.5 on 2021-08-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kmooc',
            name='image',
            field=models.CharField(max_length=255, verbose_name='image'),
        ),
    ]
