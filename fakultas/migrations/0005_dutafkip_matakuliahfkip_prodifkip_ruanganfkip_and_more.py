# Generated by Django 4.1.1 on 2022-10-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0004_alter_akreditasifkip_nilai'),
    ]

    operations = [
        migrations.CreateModel(
            name='DutaFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliahFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProdiFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RuanganFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UkmFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]