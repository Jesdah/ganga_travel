# Generated by Django 3.2.20 on 2023-08-07 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_adventure_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventure',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_adventure', to=settings.AUTH_USER_MODEL),
        ),
    ]
