from django.forms import (
    ModelForm,
)

from apps.team.models.team import Team

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = [
            'delegated',
            'name',
        ]