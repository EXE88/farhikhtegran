# Generated by Django 5.1.3 on 2024-12-10 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('homeworks', '0004_alter_homework_description'),
        ('lessons', '0003_alter_lesson_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='for_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='برای کلاس'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='for_lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='برای درس'),
        ),
    ]