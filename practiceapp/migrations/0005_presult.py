# Generated by Django 4.0.4 on 2022-05-31 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('practiceapp', '0004_practice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presult',
            fields=[
                ('presult_id', models.AutoField(primary_key=True, serialize=False)),
                ('presult_accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('presult_speed', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('presult_time', models.IntegerField()),
                ('presult_false_num', models.IntegerField()),
                ('presult_summary', models.CharField(max_length=64)),
                ('practice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practiceapp.practice')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
