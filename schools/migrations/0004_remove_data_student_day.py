# Generated by Django 2.1.3 on 2018-12-01 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_data_student_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='student_day',
        ),
    ]