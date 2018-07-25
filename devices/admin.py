import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse


from .models import Device


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]


    # write the header row
    writer.writerow([field.verbose_name for field in fields])

    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'



class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'device_name',
        'device_type',
        'device_os',
        'device_location',
        'house_lan_ip',
        'house_ip_type',
        'media_lan_ip',
        'media_ip_type',
        'hispeed_ip',
        'hispeed_ip_type'
    ]
    list_filter = ['device_os', 'device_type', 'device_location', ]
    actions = [export_to_csv]

admin.site.register(Device, DeviceAdmin)
