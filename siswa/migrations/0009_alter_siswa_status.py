# Generated by Django 4.2.3 on 2023-09-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0008_alter_siswa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='status',
            field=models.CharField(choices=[('do', 'Drop Out'), ('lulus', 'Lulus'), ('aktif', 'Aktif')], default='Aktif', max_length=20),
        ),
    ]