# Generated by Django 3.0.1 on 2019-12-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oK', '0002_auto_20191229_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitaplar',
            options={'verbose_name_plural': 'Kitaplarım'},
        ),
        migrations.AddField(
            model_name='kitaplar',
            name='yayinevi',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]