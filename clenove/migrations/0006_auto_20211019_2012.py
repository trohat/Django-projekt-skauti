# Generated by Django 3.2.7 on 2021-10-19 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0005_alter_skaut_oddil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulice', models.CharField(max_length=30)),
                ('cislo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='oddil',
            name='sidlo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clenove.adresa'),
        ),
    ]
