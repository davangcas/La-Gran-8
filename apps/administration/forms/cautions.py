import django.forms as forms
from django.forms import fields

from apps.team.models.amontestados import Amonestacion

class CautionsMultipleForm(forms.Form):

    extra_field_count = forms.CharField(widget=forms.HiddenInput())
    player = forms.TypedMultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Jugador",
    )
    team = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs= {
                    "class": "select2 select2-hidden-accessible",
                    "style": "width: 100%;",
                }),
        label="Equipo",
    )

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)
        local_players = kwargs.pop('local_players')
        super(CautionsMultipleForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        self.fields['player'].queryset = local_players
        for index in range(int(extra_fields)):
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()

