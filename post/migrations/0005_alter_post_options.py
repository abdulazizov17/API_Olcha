# Generated by Django 5.1.1 on 2024-10-11 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_publish', 'Can publish posts'), ('can_view_private', 'Can view private posts')]},
        ),
    ]
