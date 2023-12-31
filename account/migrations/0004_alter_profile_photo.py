# Generated by Django 4.2.3 on 2023-08-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True, default="None", upload_to="users/%Y/%m/%d/"
            ),
            preserve_default=False,
        ),
    ]
