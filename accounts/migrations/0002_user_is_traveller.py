# Generated by Django 2.2.9 on 2020-03-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_traveller',
            field=models.BooleanField(default=False, verbose_name='Traveller Status'),
        ),
    ]
