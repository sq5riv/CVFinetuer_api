# Generated by Django 5.1.1 on 2024-11-05 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_experience_end_date_alter_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to='foto/'),
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=50)),
                ('offer_link', models.URLField(blank=True, null=True)),
                ('offer', models.CharField(max_length=2000)),
                ('cv', models.CharField(max_length=2000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
    ]