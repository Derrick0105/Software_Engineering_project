# Generated by Django 2.1.4 on 2019-01-03 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jub_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('logo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Location_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loaction', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='jub_list',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Location_set'),
        ),
    ]
