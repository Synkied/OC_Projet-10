# Generated by Django 2.0.3 on 2018-03-26 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField()),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=500)),
                ('nutri_grade', models.CharField(max_length=1, null=True)),
                ('energy', models.IntegerField(null=True)),
                ('fat', models.FloatField(null=True)),
                ('carbs', models.FloatField(null=True)),
                ('sugars', models.FloatField(null=True)),
                ('fibers', models.FloatField(null=True)),
                ('proteins', models.FloatField(null=True)),
                ('salt', models.FloatField(null=True)),
                ('img', models.URLField(null=True)),
                ('img_small', models.URLField(null=True)),
                ('last_modified_t', models.DateTimeField()),
                ('brands', models.ManyToManyField(db_table='products_brands', to='products.Brand')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(db_table='products_stores', to='products.Store'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='substitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_substitute_set', to='products.Product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
