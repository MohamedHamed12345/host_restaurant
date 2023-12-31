# Generated by Django 4.2.2 on 2023-08-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('house', models.CharField(max_length=100)),
                ('road', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('delivery_time', models.CharField(max_length=50)),
                ('min_order', models.IntegerField(default=0)),
                ('rate', models.DecimalField(decimal_places=0, max_digits=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('restaurant', models.ManyToManyField(blank=True, to='restaurants.restaurant')),
            ],
        ),
    ]
