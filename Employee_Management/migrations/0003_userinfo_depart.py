# Generated by Django 3.2.18 on 2023-03-19 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_Management', '0002_userinfo_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee_Management.department'),
        ),
    ]
