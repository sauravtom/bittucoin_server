# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GiftCard(models.Model):

    gift_card_name = models.CharField(max_length=100)
    gift_card_discription = models.TextField()
    gift_card_image = models.CharField(max_length=100)
    gift_card_price = models.CharField(max_length=10)

    def __unicode__(self):

        return self.gift_card_name