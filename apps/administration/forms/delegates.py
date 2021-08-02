from django.forms import ModelForm
from django.contrib.auth.models import User

from apps.administration.models.users import Administrator

class DelegateForm(ModelForm):
    class Meta:
        model = Administrator
        fields = [
            'dni'
        ]

class DelegateUserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]