# Generated by Django 3.1.4 on 2020-12-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='pizzashop/images'),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
