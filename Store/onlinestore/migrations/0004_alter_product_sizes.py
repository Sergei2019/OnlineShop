# Generated by Django 3.2.16 on 2022-12-18 07:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='XS', max_length=2),
        ),
    ]
