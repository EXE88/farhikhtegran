# Generated by Django 5.1.3 on 2024-12-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0003_alter_homework_created_at_alter_homework_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.TextField(max_length=500, verbose_name='توضیحات'),
        ),
    ]