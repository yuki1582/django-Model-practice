# Generated by Django 4.1.7 on 2023-03-12 16:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0002_add_student_school_prefecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'places',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 56, 8, 174532, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 16, 56, 8, 174584, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ModelApp.places')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]