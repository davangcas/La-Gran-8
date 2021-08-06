from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from apps.administration.models.users import Administrator

def user_validator(view_function):

    def validation(request, *args, **kwargs):
        if request.user.administrator.role == "Delegado":
            return redirect('administration:indexd')
        else:
            return view_function(request, *args, **kwargs)

    return validation