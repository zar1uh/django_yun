# Generated by Django 2.0.1 on 2018-01-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('_file_name', models.CharField(default='', max_length=225, verbose_name='文件名称')),
                ('_file_type', models.CharField(choices=[('apk', 'apk'), ('exe', 'exe'), ('unknow', 'unknow')], default='', max_length=50)),
                ('_file_size', models.IntegerField(default=0, verbose_name='文件大小')),
                ('_file_path', models.CharField(default='', max_length=225, verbose_name='文件路径')),
                ('file_md5', models.CharField(default='', max_length=50)),
                ('_upload_data', models.DateField(auto_now=True)),
                ('_upload_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
