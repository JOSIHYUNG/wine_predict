# Generated by Django 2.0.3 on 2018-04-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winedata',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='winedata',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='winedata',
            name='rating',
            field=models.IntegerField(verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='winedata',
            name='region',
            field=models.CharField(max_length=20, verbose_name='region'),
        ),
    ]
