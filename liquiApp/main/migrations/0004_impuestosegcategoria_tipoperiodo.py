# Generated by Django 5.0.3 on 2024-03-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_apellidomat_usuario_apellidomat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='impuestosegcategoria',
            name='tipoperiodo',
            field=models.CharField(default='202312', max_length=10),
            preserve_default=False,
        ),
    ]
