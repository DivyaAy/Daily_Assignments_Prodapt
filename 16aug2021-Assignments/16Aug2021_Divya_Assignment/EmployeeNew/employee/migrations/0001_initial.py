# Generated by Django 3.2.6 on 2021-08-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Emp_ID', models.IntegerField()),
                ('Emp_desi', models.CharField(max_length=50)),
                ('Emp_salary', models.IntegerField()),
            ],
        ),
    ]
