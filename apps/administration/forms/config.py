from django.forms import ModelForm

from apps.administration.models.config import GeneralConfig


class GeneralConfigForm(ModelForm):

    class Meta:
        model = GeneralConfig
        fields = [
            'players_requisit',
        ]
