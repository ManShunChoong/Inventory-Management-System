# Generated by Django 5.1.3 on 2024-11-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('name', 'supplier'), name='unique_name_supplier'),
        ),
    ]