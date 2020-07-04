# Generated by Django 3.0.7 on 2020-07-03 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Api')),
            ],
        ),
    ]