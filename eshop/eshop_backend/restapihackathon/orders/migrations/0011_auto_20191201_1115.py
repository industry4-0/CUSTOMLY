# Generated by Django 2.2.7 on 2019-12-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20191130_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderHashCompleted',
        ),
        migrations.AddField(
            model_name='order',
            name='orderDate',
            field=models.DateField(auto_now=True),
        ),
    ]
