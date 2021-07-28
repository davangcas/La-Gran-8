from django.views.generic import (
    CreateView, 
    ListView, 
    DeleteView, 
    UpdateView,
    )
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import (
    render, 
    redirect,
    )