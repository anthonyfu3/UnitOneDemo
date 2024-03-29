# Generated by Django 4.2.7 on 2023-12-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fuel_notes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aircraftnote",
            name="vacuum_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="catering_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="customer_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("based_tenant", "Based Tenant"),
                    ("signature_silver", "Signature Status Silver"),
                    ("signature_gold", "Signature Status Gold"),
                    ("signature_platinum", "Signature Status Platinum"),
                ],
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="fuel_format",
            field=models.CharField(
                blank=True,
                choices=[("lbs", "lbs"), ("kgs", "kgs"), ("gallons", "gallons")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="fuel_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("jet_a_neg", "Jet-"),
                    ("jet_a_pos", "Jet+"),
                    ("avgas", "Avgas"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="gpu_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("stage", "Stage"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="ladder_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="location",
            field=models.CharField(
                choices=[
                    ("hanger_1", "H1"),
                    ("hanger_2", "H2"),
                    ("hanger_3", "H3"),
                    ("hanger_4", "H4"),
                    ("row_1", "R1"),
                    ("row_2", "R2"),
                    ("row_3", "R3"),
                    ("row_4", "R4"),
                    ("row_5", "R5"),
                    ("row_6", "R6"),
                    ("tie_down", "T-D"),
                    ("gama", "Gama"),
                    ("off_ramp", "O-R"),
                    ("customs", "Cstm"),
                    ("netjets", "NJ"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="oil_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aircraftnote",
            name="water_service_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("active", "Active"),
                    ("completed", "Completed"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
