# Generated by Django 3.2.7 on 2021-10-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skaut',
            fields=[
                ('prezdivka', models.CharField(max_length=100)),
                ('vek', models.IntegerField()),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
    ]
