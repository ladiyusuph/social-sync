# Generated by Django 5.0.1 on 2024-02-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_contact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["-created"]},
        ),
    ]
