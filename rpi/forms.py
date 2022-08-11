from django.forms import ModelForm


from .models import RaspberryPiModel, RaspberryPi, RaspberryPiSettings, RaspberryPiURLs, Location

class RaspberryPiModelForm(ModelForm):
    class Meta:
        model = RaspberryPiModel
        fields = ['name']
        labels = {
            'name': 'Model'
        }
  

    def __init__(self, *args, **kwargs):
        super(RaspberryPiModelForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class RaspberryPiForm(ModelForm):
    class Meta:
        model = RaspberryPi
        fields = ['name', 'serial_number', 'model']

    def __init__(self, *args, **kwargs):
        super(RaspberryPiForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class RaspberryPiSettings(ModelForm):
    class Meta:
        model = RaspberryPiSettings
        fields = ['tab_switch_delay']

    def __init__(self, *args, **kwargs):
        super(RaspberryPiSettings, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class RaspberryPiURLs(ModelForm):
    class Meta:
        model = RaspberryPiURLs
        fields = ['name', 'url']

    def __init__(self, *args, **kwargs):
        super(RaspberryPiURLs, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
