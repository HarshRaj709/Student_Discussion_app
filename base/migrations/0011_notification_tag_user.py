# Generated by Django 4.2.5 on 2024-03-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='tag_user',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
