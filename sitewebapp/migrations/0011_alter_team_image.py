# Generated by Django 3.2.3 on 2021-05-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0010_auto_20210526_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.FileField(upload_to='image_team'),
        ),
    ]
