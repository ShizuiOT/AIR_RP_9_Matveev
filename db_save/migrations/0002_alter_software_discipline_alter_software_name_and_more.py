# Generated by Django 4.1.3 on 2022-11-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_save', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='Discipline',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='software',
            name='Name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='software',
            name='OpSys',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='software',
            name='Practicum_Num',
            field=models.TextField(),
        ),
    ]
