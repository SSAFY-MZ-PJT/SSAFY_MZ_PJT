# Generated by Django 4.2.16 on 2024-11-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile/default_user.png', null=True, upload_to='profile/'),
        ),
    ]