# Generated by Django 4.0.4 on 2022-05-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upractice',
            fields=[
                ('upractice_id', models.AutoField(primary_key=True, serialize=False)),
                ('upractice_title', models.CharField(max_length=32)),
                ('upractice_content', models.TextField()),
                ('upractice_result', models.TextField()),
                ('upractice_chnum', models.IntegerField()),
            ],
        ),
    ]
