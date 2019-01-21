# Generated by Django 2.0.6 on 2019-01-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='用户名'),
        ),
    ]
