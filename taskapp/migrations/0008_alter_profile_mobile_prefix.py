# Generated by Django 3.2.20 on 2023-08-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0007_auto_20230820_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_prefix',
            field=models.CharField(choices=[('083', '083'), ('085', '085'), ('086', '086'), ('087', '087')], default='---', max_length=3),
        ),
    ]
