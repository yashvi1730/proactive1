# Generated by Django 3.0.7 on 2020-06-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200622_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_age_first_period', models.IntegerField()),
                ('m_date_last_period', models.DateField()),
                ('m_cycle_len', models.IntegerField()),
                ('m_period_len', models.IntegerField()),
                ('m_flow_amount', models.CharField(default='Medium', max_length=100)),
                ('m_pain_scale', models.CharField(default='Medium', max_length=100)),
                ('m_bleeding', models.CharField(default='N', max_length=100)),
            ],
        ),
    ]