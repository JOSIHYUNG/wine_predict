# Generated by Django 2.0.3 on 2018-04-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WineData',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('region', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
