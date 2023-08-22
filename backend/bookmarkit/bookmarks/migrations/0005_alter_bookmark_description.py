# Generated by Django 4.2.4 on 2023-08-22 17:50

import core.enums
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookmarks", "0004_alter_urltype_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmark",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="add a description of the collection",
                max_length=core.enums.Limits[
                    "COLLECTION_DESCRIPTION_MAX_CHAR"
                ],
                null=True,
                verbose_name="description",
            ),
        ),
    ]
