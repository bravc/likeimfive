# Generated by Django 2.0.6 on 2018-06-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='none', max_length=25),
            preserve_default=False,
        ),
    ]