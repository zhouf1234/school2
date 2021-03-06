# Generated by Django 2.1.3 on 2019-03-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuwrite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('answer', models.TextField(null=True, verbose_name='作业答案')),
                ('message', models.CharField(max_length=255, null=True, verbose_name='学生留言')),
                ('frac', models.CharField(max_length=255, null=True, verbose_name='老师打分')),
                ('ask', models.CharField(max_length=255, null=True, verbose_name='老师评语')),
                ('is_sub', models.BooleanField(default=False, verbose_name='学生是否提交')),
                ('is_cor', models.BooleanField(default=False, verbose_name='老师是否批改')),
                ('stu', models.CharField(max_length=255, null=True, verbose_name='学生姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='题目')),
                ('remarks', models.CharField(max_length=255, null=True, verbose_name='作业要求')),
                ('subject', models.CharField(max_length=255, null=True, verbose_name='科目')),
                ('teacher', models.CharField(max_length=255, null=True, verbose_name='出题老师')),
                ('days', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
            ],
        ),
    ]
