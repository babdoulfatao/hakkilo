# Generated by Django 4.0.2 on 2022-03-01 16:09

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
            name='organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_org', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('ville_org', models.CharField(max_length=255)),
                ('pays', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=255)),
                ('Organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hakkillo.organisation')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='intent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255, verbose_name='Titre')),
                ('commentaire', models.CharField(max_length=255)),
                ('pattern', models.JSONField(default=list, verbose_name='Question')),
                ('response', models.JSONField(default=list, verbose_name='Reponse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
