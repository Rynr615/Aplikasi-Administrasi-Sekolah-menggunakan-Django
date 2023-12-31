# Generated by Django 4.2.3 on 2023-09-05 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Mapel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ganjil', 'Ganjil'), ('genap', 'Genap')], max_length=10)),
                ('sekarang', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TahunPelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('sekarang', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='BiayaPendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uang_masuk', models.CharField(max_length=200)),
                ('tahun_pelajaran', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='utama.tahunpelajaran')),
            ],
            options={
                'ordering': ['tahun_pelajaran'],
            },
        ),
    ]
