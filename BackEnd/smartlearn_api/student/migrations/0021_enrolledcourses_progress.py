# Generated by Django 5.1.4 on 2025-02-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_progress_course_alter_progress_time_watched'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolledcourses',
            name='progress',
            field=models.BigIntegerField(default=0),
        ),
    ]
