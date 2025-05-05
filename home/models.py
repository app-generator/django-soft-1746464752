# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    submission-dt = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Members(models.Model):

    #__Members_FIELDS__
    fname = models.TextField(max_length=255, null=True, blank=True)
    lname = models.TextField(max_length=255, null=True, blank=True)
    gradyr = models.IntegerField(null=True, blank=True)
    username = models.BooleanField()
    password = models.BooleanField()

    #__Members_FIELDS__END

    class Meta:
        verbose_name        = _("Members")
        verbose_name_plural = _("Members")



#__MODELS__END
