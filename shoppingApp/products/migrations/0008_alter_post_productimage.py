# Generated by Django 3.2 on 2021-05-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_post_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='productImage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
