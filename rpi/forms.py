from django.forms import ModelForm


from .models import RaspberryPiModel

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
