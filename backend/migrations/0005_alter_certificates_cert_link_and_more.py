# Generated by Django 5.1.1 on 2024-11-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_knowledge_level_skills_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='cert_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]