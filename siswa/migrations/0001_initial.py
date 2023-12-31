# Generated by Django 4.2.3 on 2023-09-07 03:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utama', '0002_alter_kelas_name_alter_semester_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('do', 'Drop Out'), ('aktif', 'Aktif'), ('lulus', 'Lulus')], default='Aktif', max_length=20)),
                ('nomor_pendaftaran', models.CharField(max_length=50, unique=True)),
                ('nama', models.CharField(max_length=200)),
                ('nama_panggilan', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('pria', 'Pria'), ('wanita', 'Wanita')], max_length=30)),
                ('tanggal_lahir', models.DateField()),
                ('tanggal_daftar', models.DateField(auto_now_add=True)),
                ('hp_orang_tua', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Hp tidak sesuai', regex='^[0-9]{10-15}$')])),
                ('alamat', models.TextField(blank=True)),
                ('keterangan', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='siswa/photo')),
                ('kelas_sekarang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utama.kelas')),
            ],
            options={
                'ordering': ['nama', 'nomor_pendaftaran'],
            },
        ),
    ]
