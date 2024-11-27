# Generated by Django 5.1.3 on 2024-11-27 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manga', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to=settings.AUTH_USER_MODEL)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='manga.manga')),
            ],
        ),
    ]
