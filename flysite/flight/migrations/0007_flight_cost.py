# Generated by Django 4.1.3 on 2022-12-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_flight_connections'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='cost',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]