# Generated by Django 2.0.3 on 2018-06-02 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0009_auto_20180602_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='attibs',
            new_name='attribs',
        ),
    ]
