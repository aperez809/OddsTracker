# Generated by Django 3.1.2 on 2020-10-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oddstracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='league',
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='oddstracker.league'),
            preserve_default=False,
        ),
    ]