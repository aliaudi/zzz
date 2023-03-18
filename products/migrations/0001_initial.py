# Generated by Django 4.1.7 on 2023-03-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brande', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='imgproduct')),
            ],
        ),
    ]
