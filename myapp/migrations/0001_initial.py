# Generated by Django 3.1.7 on 2021-02-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('protein', models.FloatField()),
                ('fats', models.FloatField()),
                ('carbs', models.IntegerField()),
            ],
        ),
    ]
