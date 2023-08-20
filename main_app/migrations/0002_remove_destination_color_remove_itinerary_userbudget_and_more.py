# Generated by Django 4.2.4 on 2023-08-20 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='color',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='userBudget',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='chosDest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_for', to='main_app.chosdest'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chosdest',
            name='destDescription',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='chosdest',
            name='destName',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='chosdest',
            name='itinerary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chos_destinations', to='main_app.itinerary'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destAddress',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destDescription',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destName',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='era',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='dateTravel',
            field=models.DateTimeField(verbose_name='Travel Date'),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
