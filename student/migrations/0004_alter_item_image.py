# Generated by Django 5.1 on 2024-08-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_item_category_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]