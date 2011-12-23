from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=30)
    org = CharField(max_length=20)
    suborg = models.CharField(max_length=20)

class Org (models.Model):
    name = models.CharField(max_length=20)
    
    ORG_TYPES = (
        ('EDU', 'Educational Institution'),
        ('COM', 'Large Corporation'),
        ('SMB', 'Small Business or Company'),
        ('STG', 'Student Group'),
        ('DPT', 'Department')
    )

    org_type = models.CharField(max_length=3, choices=ORG_TYPES)
    parent = models.ForeignKey(Org)
    members = models.ManyToManyField(UserProfile)

#class assocs (Models.model):
#    user = models.ForeignKey(UserProfile)
#    org = models.(Org)
        
# Create your models here.
