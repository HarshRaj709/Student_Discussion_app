# Generated by Django 4.2.5 on 2024-03-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_notification_tag_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='room',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]