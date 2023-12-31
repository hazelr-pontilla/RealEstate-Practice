# Generated by Django 4.2.2 on 2023-06-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('sqrt', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.IntegerField()),
            ],
        ),
    ]
