# Generated by Django 4.1.3 on 2022-11-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2w_app', '0002_alter_activity_distance_alter_activity_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.PositiveIntegerField(),
        ),
    ]
