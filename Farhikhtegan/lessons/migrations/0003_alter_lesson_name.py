# Generated by Django 5.1.3 on 2024-12-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_lesson_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام درس'),
        ),
    ]