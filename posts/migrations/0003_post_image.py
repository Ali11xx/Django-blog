# Generated by Django 4.2.6 on 2023-10-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='Posts'),
            preserve_default=False,
        ),
    ]
