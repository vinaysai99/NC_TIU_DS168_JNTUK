# Generated by Django 3.0.8 on 2020-07-29 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AlterField(
            model_name='student',
            name='stuclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Class'),
        ),
    ]
