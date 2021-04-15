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



class MatrixAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Настройка матрицы', {
                'classes': ('collapse', 'extrapretty'),
                'fields': ( 'title', 'bsTsmIn', 'bsTsmOut', )
            }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('aggregator', ),
            }),
        )


@admin.register(models.Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'address', 'tsm', 'bs')
    fieldsets = (
            ('Описание', {
                'classes': ('wide', 'extrapretty'),
                'fields': ( 'title', 'city', 'address', )
            }),
            ('Подключение', {
                'classes': ('collapse', 'extrapretty'),
                'fields': ('vertical', 'plinth', 'pair',)
            }),
            ('Объект в системе', {
                'classes': ('collapse', 'extrapretty'),
                'fields': ('ts0', 'tx' , 'bs' , 'ts1' , 'tsm'  ,)
            }),
        )

admin.site.register(models.Matrix, MatrixAdmin)
# admin.site.register(models.Object, ObjectAdmin)




