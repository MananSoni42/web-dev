# Generated by Django 3.0.4 on 2020-04-10 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20200410_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Order'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Order'),
        ),
        migrations.AlterField(
            model_name='platter',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Order'),
        ),
        migrations.AlterField(
            model_name='salad',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Order'),
        ),
        migrations.AlterField(
            model_name='sub',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Order'),
        ),
    ]
