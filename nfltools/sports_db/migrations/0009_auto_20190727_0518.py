# Generated by Django 2.1.5 on 2019-07-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_db', '0008_auto_20190727_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasons',
            name='season_id',
            field=models.CharField(max_length=10),
        ),
    ]
