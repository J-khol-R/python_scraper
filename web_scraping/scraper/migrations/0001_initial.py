# Generated by Django 5.0.2 on 2024-02-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hockey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('ot_losses', models.IntegerField()),
                ('win_percentage', models.FloatField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
                ('plus_minus', models.IntegerField()),
            ],
        ),
    ]
