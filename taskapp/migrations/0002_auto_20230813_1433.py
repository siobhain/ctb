# Generated by Django 3.2.20 on 2023-08-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Suggest'), (1, 'Approved')], default=0),
        ),
    ]
