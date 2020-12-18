from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.urls import reverse
from django import forms

def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class t_sheq(models.Model):
    QUESTION_CHOCE = (
        ('Minor Injury', 'Minor Injury'),
        ('Serious Injury',
         'Serious Injury'),
        ('Fatality',
         'Fatality'),
        ('Damage to property', 'Damage to property'),
        ('Increased Cost', 'Increased Cost'),
        ('Loss of production', 'Loss of production'),
        ('Environment Impact', 'Environment Impact'),
        ('Health threat', 'Health threat')
        
    )
    LOCATION_CHOCE = (
        ('WorkShop', 'WorkShop'),
        ('Warehouse',
         'Warehouse')
         
    )
    BEHAVIOR_CHOCE = (
        ('Intentional', 'Intentional'),
        ('Unintentional',
         'Unintentional')
        
    )
    rootid = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(choices=LOCATION_CHOCE, max_length=100, null=True, blank=True)
    what_you_saw = models.CharField(max_length=500)
    reasons = models.CharField(max_length=250)
    behavior = models.CharField(choices=BEHAVIOR_CHOCE, max_length=50)
    possible_results = MultiSelectField(choices=QUESTION_CHOCE, null=True, blank=True)
    what_you_did = models.CharField(max_length=20, null=True, blank=True)
    user = models.IntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return 't_sheq {}'.format(self.id)