# Generated by Django 3.2 on 2021-05-03 18:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210503_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='productDetails',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]