# Generated by Django 3.0.14 on 2022-02-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_reward_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='reward_point',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
