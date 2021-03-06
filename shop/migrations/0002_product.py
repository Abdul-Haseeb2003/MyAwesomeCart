# Generated by Django 3.0.5 on 2020-04-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('product_desc', models.CharField(default='', max_length=500)),
                ('pub_date', models.DateField(default='20/4/2020')),
                ('image', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
