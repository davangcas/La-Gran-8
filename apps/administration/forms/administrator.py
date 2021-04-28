from django.forms import ModelForm

from apps.administration.models.users import Administrator

class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = []