from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    FormView,
    DeleteView,
    DetailView,
    TemplateView,
)
from cutting_performance.models import (
    NaturalStone,
    Abrasive,
    CuttingData
)


# HOME PAGE ---------------------------------------------------------
class HomeView(TemplateView):
    template_name = "cutting_performance/home.html"
    def get_context_data(self):
        context = super().get_context_data()
        context["stones"] = NaturalStone.objects.all()
        context["abrasives"] = Abrasive.objects.all()
        context["cutting_data"] = CuttingData.objects.all()

        return context

# ADD STONE, ABRASIVE, CUTTING DATA ---------------------------------
class StonesAdd(CreateView):
    model = NaturalStone
    template_name = "cutting_performance/add.html"
    success_url = reverse_lazy("cut:stones-add")
    fields = "__all__"

class AbrasivesAdd(CreateView):
    model = Abrasive
    template_name = "cutting_performance/add.html"
    success_url = reverse_lazy("cut:abrasives-add")
    fields = "__all__"

class CuttingDataAdd(CreateView):
    model = CuttingData
    template_name = "cutting_performance/add.html"
    success_url = reverse_lazy("cut:cutting-data-add")
    fields = "__all__"

# DETAILS OF EACH MODEL ---------------------------------------------
class StoneDetail(DetailView):
    model = NaturalStone
    template_name = "cutting_performance/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'stone'
        return context

class AbrasiveDetail(DetailView):
    model = Abrasive
    template_name = "cutting_performance/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'abrasive'
        return context

class CuttingDataDetail(DetailView):
    model = CuttingData
    template_name = "cutting_performance/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'cutting-data'
        return context

# UPDATE FIELDS IN EACH MODEL ---------------------------------------
class StoneUpdate(UpdateView):
    model = NaturalStone
    template_name = "cutting_performance/update.html"
    def get_success_url(self):
        stone_id = self.object.id
        return reverse_lazy("cut:stone-update", kwargs={"pk":stone_id})  
    fields = "__all__"

class AbrasiveUpdate(UpdateView):
    model = Abrasive
    template_name = "cutting_performance/update.html"
    def get_success_url(self):
        abrasive_id = self.object.id
        return reverse_lazy("cut:abrasive-update", kwargs={"pk":abrasive_id})  
    fields = "__all__"

class CuttingDataUpdate(UpdateView):
    model = CuttingData
    template_name = "cutting_performance/update.html"
    def get_success_url(self):
        cutting_data_id = self.object.id
        return reverse_lazy("cut:cutting-data-update", kwargs={"pk":cutting_data_id})    
    fields = "__all__"

# DELETE EACH ELEMENT IN MODELS -------------------------------------
class StoneDelete(DeleteView):
    model = NaturalStone
    success_url = reverse_lazy("cut:home")
    template_name = "cutting_performance/detail.html"

class AbrasiveDelete(DeleteView):
    model = Abrasive
    success_url = reverse_lazy("cut:home")
    template_name = "cutting_performance/detail.html"

class CuttingDataDelete(DeleteView):
    model = CuttingData
    success_url = reverse_lazy("cut:home")
    template_name = "cutting_performance/detail.html"    
