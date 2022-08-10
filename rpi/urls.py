from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rpi'

urlpatterns = [
   path('models/', views.rPiModelsList.as_view(), name='view_models'), 
   path('models/add-model/', views.rPiModelsAdd.as_view(), name='add_model'), 
   path('models/edit/<int:pk>', views.rPiModelsEdit.as_view(), name='edit_model'), 
   path('models/delete/<int:pk>', views.rPiModelsDelete.as_view(), name='delete_model'), 
]
    