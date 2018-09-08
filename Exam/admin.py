# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import PersonDetail,Location

admin.site.register(PersonDetail)
admin.site.register(Location)
