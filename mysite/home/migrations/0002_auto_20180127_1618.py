# Generated by Django 2.0.1 on 2018-01-27 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='students',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
    ]
