# Generated by Django 5.0.1 on 2024-02-06 00:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_images_delete_image_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Images",
            new_name="Image",
        ),
        migrations.RenameIndex(
            model_name="image",
            new_name="images_imag_created_17cf61_idx",
            old_name="images_imag_created_01b460_idx",
        ),
    ]
