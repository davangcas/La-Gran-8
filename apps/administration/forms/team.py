from django.forms import (
    ModelForm,
    Select
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
        widgets = {
            "delegated": Select(
                attrs= {
                    "class": "form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
        }

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
