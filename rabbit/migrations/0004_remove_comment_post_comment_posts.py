# Generated by Django 4.2 on 2023-04-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0003_profile_delete_totalcarrots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='posts',
            field=models.ManyToManyField(to='rabbit.post'),
        ),
    ]
