from apps.team.models.team import Team
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.administration.decorators import user_validator
from apps.team.models.tournament import Group, GroupTable
from apps.administration.services import check_tournament_active


class GroupDetailView(DetailView):
    model = Group
    template_name = "administration/specific/groups/detail.html"

    @method_decorator(user_validator)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(self.get_object().group_name)
        context['form_title'] = "Detalles del " + str(self.get_object().group_name)
        context['header_page_title'] = "Detalles del " + str(self.get_object().group_name)
        context['active_tournament'] = check_tournament_active()
        context['standings'] = GroupTable.objects.filter(group_play_off=self.get_object())
        return context

