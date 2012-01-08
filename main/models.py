from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=30)
    #org = models.CharField(max_length=20)
    #suborg = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.user.first_name

class Org (models.Model):
    name = models.CharField(max_length=20)
    
    ORG_TYPES = (
        ('EDU', 'Educational Institution'),
        ('COM', 'Large Corporation'),
        ('SMB', 'Small Business or Company'),
        ('STG', 'Student Group'),
        ('DPT', 'Department')
    )

    creator = models.ForeignKey(UserProfile, related_name='creator')
    org_type = models.CharField(max_length=3, choices=ORG_TYPES)
    parent = models.ForeignKey('self', blank=True, null=True)
    accepted = models.BooleanField()
    members = models.ManyToManyField(UserProfile, through='Membership')
    
    def __unicode__(self):
        return self.name

class Membership (models.Model):
    user = models.ForeignKey(UserProfile)
    org = models.ForeignKey(Org)
    accepted = models.BooleanField()

# Create your models here.
