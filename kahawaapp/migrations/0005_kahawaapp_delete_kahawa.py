# Generated by Django 5.1.1 on 2024-10-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kahawaapp', '0004_merge_20241001_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kahawaapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Kahawa',
        ),
    ]
