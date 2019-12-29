# Generated by Django 3.0.1 on 2019-12-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oK', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitaplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=500)),
                ('yazar', models.CharField(max_length=500)),
                ('konu', models.CharField(max_length=500)),
                ('notlarim', models.CharField(max_length=1500)),
                ('okudugum_sene', models.DateField()),
                ('basim_yili', models.DateField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='myBooks')),
                ('eklenme_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Kitaplarim',
        ),
    ]