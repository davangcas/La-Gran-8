from django.forms import ModelForm, Select, SelectMultiple

from apps.team.models.tournament import Tournament, League

class TournamentForm(ModelForm):
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
        fields = "__all__"
