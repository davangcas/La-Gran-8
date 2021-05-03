from django.forms import ModelForm
from django.contrib.auth.models import User

from apps.administration.models.users import Administrator

class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = [
            
        ]

class UserFormNew(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]