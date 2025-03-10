# Generated by Django 3.0.6 on 2020-06-16 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideosDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('video_img', models.ImageField(null=True, upload_to='videos/', verbose_name='')),
                ('views', models.PositiveIntegerField(default=0)),
                ('level', models.CharField(choices=[('상', '상'), ('중', '중'), ('하', '하')], default='하', max_length=5)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('skeleton', models.TextField()),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
