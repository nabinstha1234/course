from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'