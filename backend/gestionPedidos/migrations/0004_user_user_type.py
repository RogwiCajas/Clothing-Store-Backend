# Generated by Django 3.1.4 on 2021-02-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_auto_20210201_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]