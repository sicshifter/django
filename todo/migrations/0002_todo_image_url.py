# Generated by Django 3.1.2 on 2020-10-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image_url',
            field=models.CharField(max_length=2083, null=True),
        ),
    ]