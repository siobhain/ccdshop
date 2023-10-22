# Generated by Django 3.2.22 on 2023-10-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='engravable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='sizeable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.CharField(default='Complete the Description ASAP', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='engrave_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='engrave_style',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='engrave_text',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='collection',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]