# Generated by Django 5.1.4 on 2025-01-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogcategorymodel_blogcommentmodel_bloglikemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcommentmodel',
            name='comment',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
