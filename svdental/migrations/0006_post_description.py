# Generated by Django 4.0.6 on 2022-07-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svdental', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]