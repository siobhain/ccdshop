# Generated by Django 3.2.22 on 2023-12-05 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20231110_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='engrave_text',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]