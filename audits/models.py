from django.db import models
from main.models import UserProfile

class Audit(models.Model):
    user = models.ForeignKey(UserProfile)
    Audit_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField("Date Created", auto_now_add=True)
    last_mod = models.DateTimeField("Last Modified", auto_now=True)
    audit_date = models.DateTimeField('Audit Date')
    purpose = models.CharField(max_length=500)
    funder = models.CharField(max_length=50)
    leader_name = models.CharField(max_length=50)
    lead_usr_id = models.ForeignKey(User)
    sub-org = models.CharField(max_length=50)
    Loc_name = models.CharField(max_length=80)
    Loc_type = models.CharField(max_length=25)
    lat= = models.FloatField()
    lng = models.FloatField()

class WeightPt(models.Model):
    audit = models.ForeignKey(Audit)
    stream_name = models.CharField(max_length=50)
    #bin_id = models.IntegerField()

    BIN_CHOICES = (
        ('LF', 'LandFill'),
        ('BC', 'Bottles and Cans'),
        ('MP', 'Mixed Paper'),
        ('CO', 'Compost'),
        ('BH', 'BioHazard'),
        ('SH', 'Sharps'),
        ('CW', 'Chemical Waste'),
        ('EW', 'E-waste'),
        ('RW', 'Radioactive Waste'),
        ('TW', 'Toxic Waste')
    )

    bin_name = models.CharField(max_length=3, choices=BIN_CHOICES)
    weight = models.FloatField()
    bin_percent = models.FloatField()

# Create your models here.
