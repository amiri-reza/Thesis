from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from cutting.models import Cut


class CuttingView(ListView):
    template_name = "cutting/result.html"
    model = Cut
    context_object_name = "results"
