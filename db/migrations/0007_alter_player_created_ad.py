# Generated by Django 4.0.2 on 2023-03-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_race_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created_ad',
            field=models.DateField(auto_now_add=True),
        ),
    ]