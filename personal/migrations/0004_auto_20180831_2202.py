# Generated by Django 2.0.5 on 2018-08-31 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_reserve_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]