# Generated by Django 2.1.4 on 2019-01-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0010_auto_20190105_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(default='登入帳號', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(default='請輸入系級', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(default='請輸入履歷', max_length=200),
        ),
    ]