# Generated by Django 5.0.3 on 2024-03-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_comment_created_at_alter_comment_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
