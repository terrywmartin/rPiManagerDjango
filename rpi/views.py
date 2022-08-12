from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.db.models.functions import Lower

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RaspberryPiModel, RaspberryPi, Location
from .forms import RaspberryPiModelForm, RaspberryPiForm, LocationForm

# Create your views here.
class rPiModelsList(LoginRequiredMixin,View):
    def get(self, request):
        models = RaspberryPiModel.objects.all()
        context = { 
            'models': models
        }
        return render(request, 'rpi/models.html', context)

class rPiModelsAdd(LoginRequiredMixin, View):
    def get(self, request):
        form = RaspberryPiModelForm()
        context = {
            'form': form,
            'next': 'rpi:view_models'
        }
        return render(request,'rpi/add-model.html', context)

    def post(self, request):
        form = RaspberryPiModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rpi:view_models')
        
        messages.error('Error creating model.')
        return render(request, 'rpi/add-model.html')

class rPiModelsEdit(LoginRequiredMixin, View):
    def get(self, request, pk):
        rpimodel = RaspberryPiModel.objects.get(id = pk)
       
        form = RaspberryPiModelForm(instance=rpimodel)
        
        context = {
            'form': form,
            'next': 'rpi:view_models'
        }
        return render(request,'rpi/add-model.html', context)

    def post(self, request, pk):
        model = RaspberryPiModel.objects.get(id = pk)
        form = RaspberryPiModelForm(request.POST,instance=model)
        if form.is_valid():
            form.save()
            return redirect('rpi:view_models')
        messages.error('Error updating model.')
        context = { 'form': form, 'next': 'rpi:view_models' }
        return render(request, 'rpi/add-model.html', context)


class rPiModelsDelete(LoginRequiredMixin,View):
    def delete(self, request, pk):
        model = RaspberryPiModel.objects.get(id = pk)
        model.delete()

        return HttpResponse('')
        #return render(request, 'rpi/partials/model-list.html', context)

class rPiList(LoginRequiredMixin, View):
    def get(self,request):
        order_by_param = request.GET.get('order_by','name')
        sort_order = request.GET.get('sort', 'asc')
      
        if sort_order == 'asc':
            rpis = RaspberryPi.objects.all().order_by(order_by_param)
        else:
            if order_by_param == 'name':
                rpis = RaspberryPi.objects.all().order_by(Lower('name').desc())
            else:
                rpis = RaspberryPi.objects.all().order_by('-checked_in')
        
        context = { 'rpis': rpis}
        return render(request, 'rpi/raspberry_pis.html', context)

class rPiAdd(LoginRequiredMixin, View):
    def get(self, request):
        form = RaspberryPiForm()
        context = { 
            'form': form,
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/add-raspberry-pi.html', context)
    def post(self, request):
        form = RaspberryPiForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('rpi:view_rpis')    

        messages.error('Error creating model.')
        context = { 'form': form }
        return render(request, 'rpi/add-raspberry-pi.html', context)

class rPiViewrPi(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/view_rpi.html', context)

class rPiEdit(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/edit_rpi.html', context)

class rPiDelete(LoginRequiredMixin, View):
    def delete(self, request, pk):
        rpi = RaspberryPi.objects.get(id = pk)
        rpi.delete()

        return HttpResponse('')

class rPiSettings(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/rpi_settings.html', context)

class rPiDeploy(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/rpi_settings.html', context)

class rPiCheckin(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/rpi_settings.html', context)

class rPiDownloadKey(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/rpi_settings.html', context)

class rPiUploadKey(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_rpis'
        }
        return render(request, 'rpi/rpi_settings.html', context)

class rPiViewLocations(LoginRequiredMixin, View):
    def get(self,request):
        locations = Location.objects.all()
        context = { 'locations': locations}
        return render(request, 'rpi/locations.html', context)

class rPiAddLocation(LoginRequiredMixin, View):
    def get(self, request):
        form = LocationForm()
        context = { 
            'form': form,
            'next': 'rpi:view_locations'
        }
        return render(request, 'rpi/location_form.html', context)

    def post(self, request):
        form = LocationForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('rpi:view_locations')    

        messages.error('Error creating Location.')
        context = { 'form': form }
        return render(request, 'rpi:location_form.html', context)

class rPiViewLocation(LoginRequiredMixin, View):
    def get(self, request, pk):

        context = {
            'next': 'rpi:view_locations'
        }
        return render(request, 'rpi/view_locations.html', context)

class rPiEditLocation(LoginRequiredMixin, View):
    def get(self, request, pk):

        location = Location.objects.get(id = pk)
        form = LocationForm(instance=location)
        context = {
            'form': form,
            'next': 'rpi:view_locations'
        }
        return render(request, 'rpi/location_form.html', context)

    def post(self, request, pk):
        location = Location.objects.get(id = pk)
        form = LocationForm(request.POST, instance=location)

        if form.is_valid:
            form.save()
            return redirect('rpi:view_locations')

        messages.error('Error updating location.')
        return render(request, 'rpi/location_form.html')

class rPiDeleteLocation(LoginRequiredMixin, View):
    def delete(self, request, pk):
        location = Location.objects.get(id = pk)
        location.delete()

        locations = Location.objects.all()
        context = { 'locations': locations }
        return render(request, 'rpi/partials/location-list.html', context)
