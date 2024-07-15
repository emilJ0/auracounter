# Generated by Django 5.0.6 on 2024-07-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('group_data', models.JSONField(null=True)),
                ('group_history', models.JSONField(null=True)),
            ],
        ),
    ]
