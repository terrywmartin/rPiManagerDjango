from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import RaspberryPiModel
from .forms import RaspberryPiModelForm

# Create your views here.
class rPiModelsList(View):
    def get(self, request):
        models = RaspberryPiModel.objects.all()
        context = { 
            'models': models
        }
        return render(request, 'rpi/models.html', context)

class rPiModelsAdd(View):
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

class rPiModelsEdit(View):
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


class rPiModelsDelete(View):
    def delete(self, request, pk):
        model = RaspberryPiModel.objects.get(id = pk)
        model.delete()

        models = RaspberryPiModel.objects.all()
        context = {
            'models': models
        }

        return render(request, 'rpi/partials/model-list.html', context)
