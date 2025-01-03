# Generated by Django 5.1.3 on 2024-12-10 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0003_alter_lesson_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_attendancea_as_from_teacher', to=settings.AUTH_USER_MODEL)),
                ('in_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
                ('to_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_attendancea_as_to_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
