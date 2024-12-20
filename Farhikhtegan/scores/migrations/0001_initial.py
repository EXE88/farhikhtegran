# Generated by Django 5.1.3 on 2024-12-06 19:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score', models.FloatField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(20)])),
                ('from_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_score_as_from_teacher', to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
                ('to_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_score_as_to_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
