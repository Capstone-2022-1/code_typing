# Generated by Django 4.0.4 on 2022-05-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('practiceapp', '0002_delete_practice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=32)),
            ],
        ),
    ]