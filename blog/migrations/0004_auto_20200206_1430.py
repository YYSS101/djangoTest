# Generated by Django 2.1.15 on 2020-02-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200206_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yukyu',
            name='riyuu',
            field=models.CharField(max_length=100, verbose_name='理由'),
        ),
    ]
