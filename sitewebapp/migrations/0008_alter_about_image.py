# Generated by Django 3.2.3 on 2021-05-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0007_reseausociaux'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
