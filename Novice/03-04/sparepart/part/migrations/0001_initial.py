# Generated by Django 2.2 on 2020-08-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sukucadang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.TextField()),
                ('jenis', models.TextField()),
                ('kendaraan', models.TextField()),
                ('jumlah', models.TextField()),
            ],
            options={
                'db_table': 'sukucadang',
            },
        ),
    ]
