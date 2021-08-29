from django.forms import ModelForm, DateInput, Select, widgets

from apps.team.models.player import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            'team',
            'name',
            'dni',
            'date_born',
        ]
        widgets = {
            'date_born': DateInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"dd/mm/yyyy",
                }
            ),
            'team':Select(
                attrs={
                    "class":"form-control select2 select2-hidden-accessible",
                    "style":"width: 100%;",
                }
            )
        }

class PlayerEditForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'dorsal',
            'dni',
            'date_born',
        ]

class PlayerCreateDelegatedForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'dni',
            'date_born',
        ]
        widgets = {
            'date_born': DateInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"dd/mm/yyyy",
                }
            ),
        }
