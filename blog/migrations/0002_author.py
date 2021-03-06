# Generated by Django 3.1.7 on 2021-03-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('telephone', models.CharField(max_length=30)),
                ('birth_year', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
