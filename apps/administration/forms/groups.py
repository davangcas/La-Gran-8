from django.forms import ModelForm
from django.forms.widgets import SelectMultiple

from apps.team.models.tournament import Group, GroupAndPlayOff, Tournament

class AddTeamToGroupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        teams = kwargs.pop('teams')
        super().__init__(*args, **kwargs)
        self.fields['teams'].queryset = teams

    class Meta:
        model = Group
        fields = ['teams']
        widgets = {
            'teams': SelectMultiple(
                attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }
            ),
        }