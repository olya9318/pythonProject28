# Generated by Django 4.1.2 on 2022-10-30 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='Название категории'),
        ),
    ]
