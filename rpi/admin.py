from django.contrib import admin
from .models import RaspberryPi, RaspberryPiModel, RaspberryPiSettings, RaspberryPiURLs, RaspberryPiDeployed
# Register your models here.

admin.site.register(RaspberryPi)
admin.site.register(RaspberryPiModel)
admin.site.register(RaspberryPiSettings)
admin.site.register(RaspberryPiURLs)
admin.site.register(RaspberryPiDeployed)