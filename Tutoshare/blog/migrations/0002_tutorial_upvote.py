# Generated by Django 2.2 on 2019-06-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
