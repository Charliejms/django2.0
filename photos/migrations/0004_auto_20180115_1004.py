# Generated by Django 2.0.1 on 2018-01-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180110_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'Pública'), ('PRI', 'Privada')], default='PUB', max_length=3),
        ),
    ]
