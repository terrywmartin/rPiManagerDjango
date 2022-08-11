from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rpi'

urlpatterns = [
   path('models/', views.rPiModelsList.as_view(), name='view_models'), 
   path('models/add-model/', views.rPiModelsAdd.as_view(), name='add_model'), 
   path('models/edit/<int:pk>', views.rPiModelsEdit.as_view(), name='edit_model'), 
   path('models/delete/<int:pk>', views.rPiModelsDelete.as_view(), name='delete_model'), 

   path('rpis/', views.rPiList.as_view(), name='view_rpis'), 
   path('rpis/add', views.rPiAdd.as_view(), name='add_rpi'), 
   path('rpis/<int:pk>', views.rPiViewrPi.as_view(), name='view_rpi'), 
   path('rpis/edit/<int:pk>', views.rPiEdit.as_view(), name='edit_rpi'), 
   path('rpis/delete/<int:pk>', views.rPiDelete.as_view(), name='delete_rpi'), 
   path('rpis/settings/<int:pk>', views.rPiSettings.as_view(), name='rpi_settings'), 
   path('rpis/deploy/<int:pk>', views.rPiDeploy.as_view(), name='rpi_deploy'), 
   path('rpis/check-in/<int:pk>', views.rPiCheckin.as_view(), name='rpi_checkin'), 
   path('rpis/key/upload/<int:pk>', views.rPiUploadKey.as_view(), name='rpi_upload_key'), 
   path('rpis/key/downlaod/<int:pk>', views.rPiDownloadKey.as_view(), name='rpi_download_key'), 

   path('locations/', views.rPiViewLocations.as_view(), name='view_locations'), 
   path('locations/<int:pk>', views.rPiViewLocation.as_view(), name='view_location'), 
   path('locations/add/', views.rPiAddLocation.as_view(), name='add_location'), 
   path('locations/edit/<int:pk>', views.rPiEditLocation.as_view(), name='edit_location'), 
   path('locations/delete/<int:pk>', views.rPiDeleteLocation.as_view(), name='delete_location'), 
]
    
    