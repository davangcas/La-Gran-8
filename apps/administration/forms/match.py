from django.forms import ModelForm, Select
from apps.team.models.match import Match
from apps.team.models.team import Team
from apps.team.models.tournament import Tournament

class MatchLeagueForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['local_team'].queryset = Tournament.objects.filter(status=True).last().teams.all()
        self.fields['away_team'].queryset = Tournament.objects.filter(status=True).last().teams.all()

    class Meta:
        model = Match
        fields = [
            'local_team',
            'away_team',
            'field',
            'date_of_match',
            'hour_of_match',
        ]
        widgets = {
            'local_team':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
            'away_team':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
            'hour_of_match':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
            'field':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
        }


class MatchLeagueEditForm(ModelForm):


    class Meta:
        model = Match
        fields = [
            'field',
            'date_of_match',
            'hour_of_match',
        ]
        widgets = {
            'hour_of_match':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
            'field':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            ),
        }


class MatchLoadResultForm(ModelForm):

    class Meta:
        model = Match
        fields = [
            'goals_local',
            'goals_away',
        ]
