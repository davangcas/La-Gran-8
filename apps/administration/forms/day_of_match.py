from django.forms import ModelForm, SelectMultiple
from django import forms

from apps.team.models.tournament import Tournament, League, ConfigTournament
from apps.team.models.team import Team
from apps.team.models.match import DateOfMatch

class DayOfMatchForm(ModelForm):

    class Meta:
        model = DateOfMatch
        fields = [
            'number',
            'day_of_match',
        ]