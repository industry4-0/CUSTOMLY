# Generated by Django 2.2.7 on 2019-11-30 10:58

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191130_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='attributes',
            field=jsonfield.fields.JSONField(default={}, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}),
        ),
    ]
