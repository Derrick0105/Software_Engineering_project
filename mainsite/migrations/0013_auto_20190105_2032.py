# Generated by Django 2.1.4 on 2019-01-05 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0012_auto_20190105_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='company',
            new_name='student',
        ),
    ]
