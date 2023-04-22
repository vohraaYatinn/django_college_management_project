# Generated by Django 4.1.7 on 2023-04-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersadmin', '0002_delete_adminusers2_adminusers_role_faculties_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidaysList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('occassion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('Message', models.TextField(blank=True)),
            ],
        ),
    ]