# Generated by Django 4.2.5 on 2024-03-23 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_notification_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room'),
        ),
    ]