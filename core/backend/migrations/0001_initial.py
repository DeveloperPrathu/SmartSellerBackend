# Generated by Django 4.1.7 on 2023-03-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]