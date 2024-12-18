# Generated by Django 5.1.2 on 2024-12-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sermons', '0002_rename_date_sermon_sermon_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayerrequest',
            name='is_responded',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='response',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='title',
        ),
        migrations.RemoveField(
            model_name='prayerrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='email',
            field=models.EmailField(default='<EMAIL>', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='name',
            field=models.CharField(default='Prayer for Family', max_length=100),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='phone_number',
            field=models.CharField(default='07', max_length=10),
        ),
        migrations.AlterField(
            model_name='prayerrequest',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
