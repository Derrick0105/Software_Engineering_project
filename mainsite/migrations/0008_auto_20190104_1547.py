# Generated by Django 2.1.4 on 2019-01-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20190104_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_list',
            name='location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='job_list',
            name='logo',
            field=models.ImageField(default='未選擇', upload_to='photos'),
        ),
    ]
