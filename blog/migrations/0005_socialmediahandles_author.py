# Generated by Django 4.1.5 on 2023-05-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_cuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediahandles',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.cuser'),
            preserve_default=False,
        ),
    ]