# Generated by Django 5.1.4 on 2025-02-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_ratingstar'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='visible_status',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=10),
        ),
    ]
