# Generated by Django 4.1.6 on 2023-02-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
