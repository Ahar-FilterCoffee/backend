# Generated by Django 5.0.6 on 2024-07-04 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('status', models.IntegerField()),
                ('fromUser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fromUser', to='api.profile')),
                ('toUser', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='toUser', to='api.profile')),
            ],
        ),
    ]
