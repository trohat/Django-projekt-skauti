# Generated by Django 3.2.7 on 2021-10-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skaut',
            options={'ordering': ['prezdivka'], 'verbose_name_plural': 'Skauti'},
        ),
        migrations.AlterField(
            model_name='skaut',
            name='slug',
            field=models.SlugField(editable=False, primary_key=True, serialize=False),
        ),
    ]