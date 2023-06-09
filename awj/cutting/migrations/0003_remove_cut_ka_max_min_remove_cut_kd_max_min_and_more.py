# Generated by Django 4.1.7 on 2023-03-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cutting", "0002_remove_cut_cakilma_bolgesi"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cut",
            name="ka_max_min",
        ),
        migrations.RemoveField(
            model_name="cut",
            name="kd_max_min",
        ),
        migrations.AddField(
            model_name="cut",
            name="dk_min",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cut",
            name="ka_max",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cut",
            name="ka_min",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cut",
            name="kd_max",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="kerf_acisi",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="kesme_asinma",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="kesme_derinligi",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="kesme_genisligi",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="plaka_agirlik_kaybi",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cut",
            name="yuzey_puruzlulugu",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
