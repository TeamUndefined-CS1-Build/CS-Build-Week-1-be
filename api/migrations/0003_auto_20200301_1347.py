# Generated by Django 3.0.3 on 2020-03-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200301_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='base_health',
            field=models.IntegerField(verbose_name='health points'),
        ),
    ]
