# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')
    #une autre methode sera de creer un model tag qui aurra comme cle etrangere la cle primaire de la table article.
    tag = models.TextField()

    def __str__(self): # if Python 2 use __unicode__
        return self.titre
