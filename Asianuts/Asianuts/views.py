from django.shortcuts import redirect, render
from django.views.generic import TemplateView
import re
# from django.contrib.auth.views import login, logout
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'template_name': 'template/base.html'
        }
        return context
    
    