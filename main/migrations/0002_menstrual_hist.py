# Generated by Django 3.0.7 on 2020-06-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menstrual_Hist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_first_period', models.IntegerField()),
                ('date_last_period', models.DateField()),
                ('cycle_len', models.IntegerField()),
                ('period_len', models.IntegerField()),
                ('flow_amount', models.CharField(default='Medium', max_length=100)),
                ('pain_scale', models.CharField(default='Medium', max_length=100)),
                ('bleeding', models.CharField(default='no', max_length=100)),
            ],
        ),
    ]