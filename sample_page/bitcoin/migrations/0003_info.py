# Generated by Django 3.1.7 on 2021-02-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bitcoin', '0002_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=200)),
                ('marketCap', models.CharField(max_length=200)),
            ],
        ),
    ]
