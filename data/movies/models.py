# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class data(models.Model):

    movie_name = models.TextField(max_length=300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() 
datetime.timedelta(days=1)    

class detail(models.Model):

	name = models.Foreignkey(data , on_delete = models.CASCADE)
    cast = models.TextField(max_length =300)
    review = models.TextField(max_length=300)