# Generated by Django 4.2.4 on 2023-08-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_blogpost_auther_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='', null=True),
        ),
    ]
