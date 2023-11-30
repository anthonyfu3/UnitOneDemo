from django.db import models

class AircraftNote(models.Model):
    STATUS_CHOICES = [
        ('incoming', 'Incoming'),
        ('departing', 'Departing'),
        ('quickturn', 'Quickturn'),
        ('off_ramp', 'Off-Ramp'),
        ('standby', 'Standby'),
        ('maintenance', 'Maintenance'),
        ('overnight', 'Overnight'),
    ]

    LOCATION_CHOICES = [
        ('hanger1', 'Hanger 1'),
        ('hanger2', 'Hanger 2'),
        ('hanger3', 'Hanger 3'),
        ('hanger4', 'Hanger 4'),
        ('storage_r1', 'Storage R1'),
        # ... additional locations as per your list ...
        ('tie_down', 'Tie-Down'),
        ('gama', 'Gama'),
        ('off_ramp', 'Off-Ramp'),
        ('customs', 'Customs'),
        ('netjets', 'NetJets'),
        # ... more locations ...
    ]

    FUEL_FORMAT_CHOICES = [
        ('lbs', 'Pounds (LBs)'),
        ('kgs', 'Kilograms (KGs)'),
        ('gallons', 'Gallons (Gs)'),
    ]

    FUEL_TYPE_CHOICES = [
        ('jet_a_neg', 'Jet-A Negative (Jet-)'),
        ('jet_a_pos', 'Jet-A Positive (Jet+)'),
        ('avgas', 'Avgas (Av)'),
    ]

    LAV_STATUS_CHOICES = [
        ('none', 'None'),
        ('fwr', 'Fwr'),
        ('aft', 'Aft'),
        ('fwr_aft', 'Fwr & Aft'),
        ('completed', 'Completed'),
    ]

    LAV_TYPE_CHOICES = [
        ('full', 'Full'),
        ('dump', 'Dump'),
        ('rinse', 'Rinse'),
    ]

    WATER_SERVICE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    GPU_STATUS_CHOICES = [
        ('stage', 'Stage'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    CUSTOMER_TYPE_CHOICES = [
        ('based_tenant', 'Based Tenant'),
        ('signature_silver', 'Signature Status Silver'),
        ('signature_gold', 'Signature Status Gold'),
        ('signature_platinum', 'Signature Status Platinum'),
    ]

    OIL_STATUS_CHOICES = [
        ('none', 'None'),
        ('required', 'Required'),
    ]

    tail_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    service_time = models.DateTimeField()
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES)
    aircraft_model = models.CharField(max_length=50)
    eta = models.DateTimeField(verbose_name='Estimated Time of Arrival', null=True, blank=True)
    etd = models.DateTimeField(verbose_name='Estimated Time of Departure', null=True, blank=True)
    passenger_count = models.IntegerField(null=True, blank=True)
    fuel_qty = models.IntegerField(verbose_name='Fuel Quantity', null=True, blank=True)
    fuel_format = models.CharField(max_length=10, choices=FUEL_FORMAT_CHOICES, null=True, blank=True)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, null=True, blank=True)
    lav_status = models.CharField(max_length=10, choices=LAV_STATUS_CHOICES, null=True, blank=True)
    lav_type = models.CharField(max_length=10, choices=LAV_TYPE_CHOICES, null=True, blank=True)
    lav_gallons = models.IntegerField(null=True, blank=True)
    water_service_status = models.CharField(max_length=10, choices=WATER_SERVICE_STATUS_CHOICES, null=True, blank=True)
    gpu_status = models.CharField(max_length=10, choices=GPU_STATUS_CHOICES, null=True, blank=True)
    catering_status = models.CharField(max_length=10, null=True, blank=True)
    catering_number = models.CharField(max_length=50, null=True, blank=True)
    pic = models.CharField(max_length=50, null=True, blank=True)  # PIC stands for Paper, Ice, Coffee
    customer_type = models.CharField(max_length=30, choices=CUSTOMER_TYPE_CHOICES, null=True, blank=True)
    oil_status = models.CharField(max_length=10, choices=OIL_STATUS_CHOICES, null=True, blank=True)
    oil_type = models.CharField(max_length=50, null=True, blank=True)
    oil_qty = models.IntegerField(null=True, blank=True)
    ladder_status = models.CharField(max_length=10, null=True, blank=True)
    vacuum_status = models
    notes = models.TextField(null=True, blank=True)
