# Generated by Django 3.2.1 on 2021-05-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0008_auto_20210512_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('comment', models.TextField(max_length=300)),
            ],
        ),
    ]
