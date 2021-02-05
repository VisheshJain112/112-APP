# Generated by Django 2.2.16 on 2021-01-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_ad_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad_user',
            name='recommendation_file',
        ),
        migrations.AddField(
            model_name='ad_admin',
            name='feedback_iframe_code',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad_admin',
            name='recommendation_file',
            field=models.FileField(default=0, upload_to='data_pool'),
            preserve_default=False,
        ),
    ]