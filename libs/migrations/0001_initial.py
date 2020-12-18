# Generated by Django 3.1.4 on 2020-12-11 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='t_sheq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
                ('what_you_saw', models.CharField(max_length=500)),
                ('reasons', models.CharField(max_length=250)),
                ('behavior', models.CharField(max_length=50)),
                ('possible_results', models.CharField(max_length=500)),
                ('what_you_did', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('rootid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]