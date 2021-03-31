# Generated by Django 3.1.2 on 2021-03-31 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210331_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='value',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='value',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=5, max_digits=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
    ]
