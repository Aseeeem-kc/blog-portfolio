# Generated by Django 4.2.4 on 2024-08-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Introduction',
        ),
        migrations.AlterField(
            model_name='expertise',
            name='description',
            field=models.TextField(),
        ),
    ]
