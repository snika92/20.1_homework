# Generated by Django 4.2.6 on 2023-10-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('date_of_creation', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('date_of_change', models.DateField(blank=True, null=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]