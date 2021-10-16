import django.forms as forms
from django.forms import fields

from apps.team.models.amontestados import Amonestacion


class CautionsForm(forms.Form):

    amonestados_local = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Amonestados",
        required=False,
    )

    expulsados_local = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Amonestados",
        required=False,
    )

    amonestados_visitante = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Amonestados",
        required=False,
    )

    expulsados_visitante = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Amonestados",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        local_players = kwargs.pop('local_players')
        away_players = kwargs.pop('away_players')
        super().__init__(*args, **kwargs)
        self.fields['amonestados_local'].queryset = local_players
        self.fields['expulsados_local'].queryset = local_players
        self.fields['amonestados_visitante'].queryset = away_players
        self.fields['expulsados_visitante'].queryset = away_players


class NewCautionsForm(forms.ModelForm):

    class Meta:
        model = Amonestacion
        fields = [
            'player',
            'type_amonestated',
        ]
