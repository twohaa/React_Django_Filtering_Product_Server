# Generated by Django 4.2.3 on 2023-08-01 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pub_date',
        ),
    ]
