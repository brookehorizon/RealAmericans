# Generated by Django 4.0 on 2022-04-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_options_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
