# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#pour que nous puissions voir notre application siteweb dans l'admin de Django.

from .models import Article

admin.site.register(Article)
