from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RecentUsage)
admin.site.register(models.BatteryUsage)
admin.site.register(models.TimeStamp)