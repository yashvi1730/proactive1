# Generated by Django 3.0.7 on 2020-06-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200622_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcos_history',
            name='q1_check1',
        ),
        migrations.RemoveField(
            model_name='pcos_history',
            name='q1_check2',
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='acne',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='diff_conceiving',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='excess_hair_growth',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='hair_loss',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='irr_period',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='none',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='other',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='poly_cystic_ovaries',
            field=models.CharField(default='n', max_length=100),
        ),
        migrations.AddField(
            model_name='pcos_history',
            name='weight_gain',
            field=models.CharField(default='n', max_length=100),
        ),
    ]
