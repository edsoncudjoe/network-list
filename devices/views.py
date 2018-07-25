from django.shortcuts import render, redirect, reverse

from .forms import AddDeviceForm
from .models import Device


def add_device(request):
    if request.method == 'POST':
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.save()
            return redirect(reverse('devices:view_devices'))
    else:
        form = AddDeviceForm()
    return render(request, 'devices/add-device.html', {'add_form':form})


def view_devices(request):
    devices = Device.objects.all()
    return render(request, 'devices/devices.html', {'devices': devices})