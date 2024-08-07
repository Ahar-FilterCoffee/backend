# Generated by Django 5.0.6 on 2024-07-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foodQUantity',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='foodType',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.URLField(default=None, null=True),
        ),
    ]
