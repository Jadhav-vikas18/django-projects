# Generated by Django 3.2.25 on 2025-05-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='summer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
                ('expiry_date', models.DateField()),
                ('manufacturing_date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='monsoon',
        ),
    ]
