# Generated by Django 4.2.2 on 2023-07-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist', models.CharField(max_length=20)),
                ('Album', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=500)),
            ],
        ),
    ]
