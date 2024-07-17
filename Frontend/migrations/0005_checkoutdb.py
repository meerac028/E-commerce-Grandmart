# Generated by Django 4.2.6 on 2024-01-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('Lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Town', models.CharField(blank=True, max_length=100, null=True)),
                ('Postcode', models.IntegerField(blank=True, null=True)),
                ('Phonenum', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]