from django.db.models import fields
from django.forms import ModelForm, SelectMultiple
from django import forms

from apps.team.models.tournament import Tournament, League, ConfigTournament, DaysOfWeek
from apps.team.models.team import Team

class TournamentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teams'].queryset = Team.objects.filter(active=True)
    
    class Meta:
        model = Tournament
        fields = [
            "name",
            "teams",
            "date_init",
            "date_finish",
            "format",
        ]
        widgets = {
            'teams': SelectMultiple(
                attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }
            ),
        }

class LeagueForm(ModelForm):

    class Meta:
        model = League
        fields = [
            'vueltas',
        ]


class ConfigTournamentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['days'].queryset = DaysOfWeek.objects.all()
        
    class Meta:
        model = ConfigTournament
        fields = [
            'days',
            'hour_init',
            'hour_end',
            'fields'
        ]
        widgets = {
            'days': SelectMultiple(
                attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }
            ),
        }
