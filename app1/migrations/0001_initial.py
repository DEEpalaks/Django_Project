# Generated by Django 4.1.2 on 2022-12-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Item', models.CharField(choices=[('1', 'OIL'), ('2', 'Grocerey'), ('3', 'Cosmetics')], default='OIL', max_length=20)),
                ('Quantity', models.IntegerField()),
                ('Rate', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
