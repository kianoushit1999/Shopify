from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class SpecificCategory(TemplateView):
    template_name = 'category.html'