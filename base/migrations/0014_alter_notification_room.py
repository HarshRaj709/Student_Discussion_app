# Generated by Django 4.2.5 on 2024-03-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_notification_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='room',
            field=models.CharField(max_length=100),
        ),
    ]
