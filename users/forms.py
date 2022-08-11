from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


from .models import User

class CustomUserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm password'
        }
  

    def __init__(self, *args, **kwargs):
        super(CustomUserModelForm, self).__init__(*args, **kwargs)
        

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
