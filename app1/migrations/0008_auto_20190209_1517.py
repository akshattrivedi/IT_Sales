# Generated by Django 2.1.5 on 2019-02-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20190209_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ques_1_id',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ques_2_id',
            field=models.CharField(max_length=5),
        ),
    ]
