# Generated by Django 3.2.1 on 2021-05-13 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estate', '0015_alter_message_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
