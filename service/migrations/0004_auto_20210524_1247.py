# Generated by Django 3.2.3 on 2021-05-24 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='sous_titre',
        ),
        migrations.AddField(
            model_name='card',
            name='categorie',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='image_card', to='service.categorie'),
            preserve_default=False,
        ),
    ]
