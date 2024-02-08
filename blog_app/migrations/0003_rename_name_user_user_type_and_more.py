# Generated by Django 5.0.2 on 2024-02-08 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_tagscategories_blog_comment_blogtags_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_type',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='content',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type_ref',
        ),
    ]