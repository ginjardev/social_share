# Generated by Django 4.2.3 on 2023-08-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actions", "0002_alter_action_target_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="action",
            name="verb",
            field=models.CharField(default="default", max_length=255),
            preserve_default=False,
        ),
    ]
