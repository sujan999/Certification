# Generated by Django 2.2 on 2019-06-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('pen', 'pending'), ('com', 'completed')], default='pen', max_length=20),
        ),
    ]
