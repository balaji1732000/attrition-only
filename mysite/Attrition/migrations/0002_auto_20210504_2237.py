# Generated by Django 2.1 on 2021-05-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attrition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attrition_table',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='attrition_table',
            name='stay_left',
        ),
        migrations.RemoveField(
            model_name='attrition_table',
            name='tenure',
        ),
        migrations.AlterField(
            model_name='attrition_table',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
