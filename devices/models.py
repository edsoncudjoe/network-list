from django.db import models


class Device(models.Model):

    LOCATION_CHOICES = (
        ('FRONT_OFFICE', 'Front Office'),
        ('MEETING_ROOM', 'Meeting Room'),
        ('EDIT_1', 'Edit 1'),
        ('EDIT_2', 'Edit 2'),
        ('EDIT_3', 'Edit 3'),
        ('EDIT_4', 'Edit 4'),
        ('MCR', 'Machine Room'),
        ('COMMS', 'Comms'),
    )

    OS_CHOICES = (
        ('OSX SnowLeopard', 'OS X Snow Leopard \(10.6\)'),
        ('OSX Lion', 'OS X Snow Lion \(10.7\)'),
        ('OSX MountainLion', 'OS X Mountain Lion \(10.8\)'),
        ('OSX Mavericks', 'OS X Mavericks \(10.9\)'),
        ('OSX Yosemite', 'OS X Yosemite \(10.10\)'),
        ('OSX ElCapitan', 'OS X El Capitan \(10.11\)'),
        ('OS Sierra', 'Mac OS Sierra \(10.12\)'),
        ('OS HiSierra', 'Mac OS HighSierra \(10.13\)'),
        ('OS Mojave', 'Mac OS Mojave \(10.14\)'),
        ('Windows 10', 'Windows 10'),
        ('Windows 7', 'Windows 7'),
        ('Windows Server 2016', 'Windows Server 2016'),
        ('Windows Server 2012 R2', 'Windows Server 2012 R2'),
        ('Windows Server 2012', 'Windows Server 2012'),
        ('Windows Server 2008 R2', 'Windows Server 2008 R2'),
        ('Windows Server 2008', 'Windows Server 2008'),
        ('Linux CentOS 5', 'Linux CentOS 5'),
        ('Linux CentOS 6', 'Linux CentOS 6'),
        ('Linux CentOS 7', 'Linux CentOS 7'),
        ('Video', 'Video Equipment'),
        ('other', 'Other'),
    )

    DEVICE_TYPE_CHOICE = (
        ('pc', 'Desktop PC'),
        ('mac', 'Desktop MAC'),
        ('server', 'Server'),
        ('video', 'Video Equipment'),
        ('Printer','printer'),
        ('Other', 'other')
    )

    IP_TYPE_CHOICES = (
        ('Static','Static'),
        ('DHCP', 'DHCP'),
        ('N/A', 'N/A')
    )


    device_name = models.CharField(max_length=256, db_index=True)
    device_type = models.CharField(max_length=256, choices=DEVICE_TYPE_CHOICE)
    device_os = models.CharField(max_length=64, choices=OS_CHOICES)
    device_location = models.CharField(max_length=128, choices=LOCATION_CHOICES)
    house_lan_ip = models.GenericIPAddressField(default='0.0.0.0')
    house_ip_type = models.CharField(max_length=64, choices=IP_TYPE_CHOICES, default='N/A')
    media_lan_ip = models.GenericIPAddressField(default='0.0.0.0')
    media_ip_type = models.CharField(max_length=64, choices=IP_TYPE_CHOICES, default='N/A')
    hispeed_ip = models.GenericIPAddressField(default='0.0.0.0')
    hispeed_ip_type = models.CharField(max_length=64, choices=IP_TYPE_CHOICES, default='N/A')


