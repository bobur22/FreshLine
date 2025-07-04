# Generated by Django 5.2.3 on 2025-07-02 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_country', models.CharField(max_length=255)),
                ('demand_level', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='export_entries', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ImportData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='import_entries', to='products.product')),
            ],
        ),
    ]
