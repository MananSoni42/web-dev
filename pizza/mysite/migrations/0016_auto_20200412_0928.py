# Generated by Django 3.0.4 on 2020-04-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20200412_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='small_price',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sub',
            name='small_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
