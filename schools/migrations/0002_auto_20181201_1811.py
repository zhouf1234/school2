# Generated by Django 2.1.3 on 2018-12-01 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=32)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Data'),
        ),
    ]
