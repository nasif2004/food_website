# Generated by Django 2.2 on 2022-04-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220409_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
