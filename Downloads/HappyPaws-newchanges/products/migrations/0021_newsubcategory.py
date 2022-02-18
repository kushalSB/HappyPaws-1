# Generated by Django 3.0.14 on 2022-02-16 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20220208_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('par_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]
