# Generated by Django 2.1.15 on 2020-03-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20200317_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='present_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
