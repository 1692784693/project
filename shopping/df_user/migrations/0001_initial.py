# Generated by Django 2.1.1 on 2018-10-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ushou', models.CharField(default='', max_length=30)),
                ('uaddress', models.CharField(default='', max_length=100)),
                ('uyoubian', models.CharField(default='', max_length=6)),
                ('uphone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
