# Generated by Django 3.1.7 on 2021-03-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210318_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Man'), ('W', 'Woman')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]