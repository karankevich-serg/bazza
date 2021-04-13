from django.contrib import admin
from . import models

class BsInTsmAdmin(admin.ModelAdmin):
    list_display = ('bs', 'title','card','led','plinth','pair')

# Register your models here.
admin.site.register(models.Timeslot)
admin.site.register(models.BsInTsm, BsInTsmAdmin)
admin.site.register(models.AggregatorsType)
admin.site.register(models.City)
admin.site.register(models.Aggregator)

admin.site.register(models.Iprobe)
admin.site.register(models.BsOutTsm)
admin.site.register(models.Direction)
admin.site.register(models.Stream)
admin.site.register(models.Matrix)