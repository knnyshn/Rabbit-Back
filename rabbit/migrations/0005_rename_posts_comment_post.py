# Generated by Django 4.2 on 2023-04-07 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rabbit', '0004_remove_comment_post_comment_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
    ]