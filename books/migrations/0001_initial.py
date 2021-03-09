# Generated by Django 3.0.5 on 2021-03-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('bookName', models.CharField(default='', max_length=50)),
                ('company', models.CharField(default='', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('genreCode', models.IntegerField()),
            ],
        ),
    ]
