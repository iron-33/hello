# Generated by Django 3.1.6 on 2022-01-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=160)),
                ('date_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
