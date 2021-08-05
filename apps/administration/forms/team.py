from django.forms import (
    ModelForm,
)

from apps.team.models.team import Team
from apps.administration.models.users import Administrator

class TeamCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delegated'].queryset = Administrator.objects.filter(role="Delegado")

    class Meta:
        model = Team
        fields = [
            'name',
            'delegated',
            'logo',
        ]

class TeamUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delegated'].queryset = Administrator.objects.filter(role="Delegado")

    class Meta:
        model = Team
        fields = [
            'name',
            'delegated',
            'logo',
        ]
