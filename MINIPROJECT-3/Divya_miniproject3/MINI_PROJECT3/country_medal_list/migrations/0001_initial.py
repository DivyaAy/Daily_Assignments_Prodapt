# Generated by Django 3.2.6 on 2021-08-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_name', models.CharField(max_length=50)),
                ('Gold_medal', models.IntegerField()),
                ('Silver_medal', models.IntegerField()),
                ('Bronze_medal', models.IntegerField()),
            ],
        ),
    ]
