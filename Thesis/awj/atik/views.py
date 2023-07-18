from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    FormView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from atik.forms import NaturalStoneForm
from atik.models import NaturalStones, MechanicalProperties, PhysicalProperties
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class HomeView(TemplateView):
    template_name = "atik/home.html"


class AddNaturalStone(FormView):
    template_name = "atik/add-stone.html"
    form_class = NaturalStoneForm
    fields = "__all__"
    # success_url = reverse_lazy("atik:home")

    def post(self, request):
        form = NaturalStoneForm(request.POST)
        if form.is_valid():
            NaturalStones.objects.create(
                name=form.cleaned_data.get("name"),
                chemical_properties=form.cleaned_data.get("chemical_properties"),
                sem_photo=form.cleaned_data.get("sem_photo"),
            )
            # breakpoint()
            stone = NaturalStones.objects.last()
            MechanicalProperties.objects.create(
                stone=stone,
                density=form.cleaned_data.get("density"),
                schmidt_hardness=form.cleaned_data.get("schmidt_hardness"),
                indirect_tensile=form.cleaned_data.get("indirect_tensile"),
                uniaxial_comp_str=form.cleaned_data.get("uniaxial_comp_str"),
                bohme=form.cleaned_data.get("bohme"),
                point_load=form.cleaned_data.get("point_load"),
                ultrasonic=form.cleaned_data.get("ultrasonic"),
            )
            PhysicalProperties.objects.create(
                stone=stone,
                su_emme_kapasitesi=form.cleaned_data.get("su_emme_kapasitesi"),
                efektif_su_emme=form.cleaned_data.get("efektif_su_emme"),
                dogal_su_icerigi=form.cleaned_data.get("dogal_su_icerigi"),
                doyma_derecesi=form.cleaned_data.get("doyma_derecesi"),
                kuru_yogunluk=form.cleaned_data.get("kuru_yogunluk"),
                doymus_yogunluk=form.cleaned_data.get("doymus_yogunluk"),
                tabii_yogunluk=form.cleaned_data.get("tabii_yogunluk"),
                mineral_tane_yogunlugu=form.cleaned_data.get("mineral_tane_yogunlugu"),
                efektif_porozite=form.cleaned_data.get("efektif_porozite"),
                toplam_porozite=form.cleaned_data.get("toplam_porozite"),
                bosluk_orani=form.cleaned_data.get("bosluk_orani"),
            )
            message = _("Natural Stone Added Successfully")
            messages.success(request, message)
            return HttpResponseRedirect(reverse_lazy("atik:add-stone"))
        return NaturalStoneForm()


class DeleteNaturalStone(DeleteView):
    model = NaturalStones
    success_url = reverse_lazy("atik:list-stone")

    def get(self, request):
        id = request.GET.get("id")
        return render(request, "list-stone", {"id": id})


class ListNaturalStone(ListView):
    model = NaturalStones
    template_name = "atik/list-stone.html"
    context_object_name = "stones"

    def get_context_data(self):
        context = super().get_context_data()
        context["stones"] = NaturalStones.objects.all()
        return context


class DetailNaturalStone(DetailView):
    model = NaturalStones
    template_name = "atik/detail-stone.html"


class UpdateNaturalStone(UpdateView):
    model = NaturalStones
    template_name = "atik/update-stone.html"
    fields = "__all__"

    def get_success_url(self):
        stone_id = self.object.id
        return reverse_lazy("atik:detail-stone", kwargs={"pk": stone_id})


class UpdatePhysicalProperties(UpdateView):
    model = PhysicalProperties
    template_name = "atik/update-stone.html"
    fields = [
        "su_emme_kapasitesi",
        "efektif_su_emme",
        "dogal_su_icerigi",
        "doyma_derecesi",
        "kuru_yogunluk",
        "doymus_yogunluk",
        "tabii_yogunluk",
        "mineral_tane_yogunlugu",
        "efektif_porozite",
        "toplam_porozite",
        "bosluk_orani",
    ]

    def get_object(self, queryset=None):
        stone_id = self.kwargs["stone_id"]
        return self.model.objects.get(stone_id=stone_id)

    def get_success_url(self):
        stone_id = self.object.id
        return reverse_lazy("atik:detail-stone", kwargs={"pk": stone_id})


class UpdateMechanicalProperties(UpdateView):
    model = MechanicalProperties
    template_name = "atik/update-stone.html"
    fields = [
        "density",
        "schmidt_hardness",
        "indirect_tensile",
        "uniaxial_comp_str",
        "bohme",
        "point_load",
        "ultrasonic",
    ]

    def get_object(self, queryset=None):
        stone_id = self.kwargs["stone_id"]
        return self.model.objects.get(stone_id=stone_id)

    def get_success_url(self):
        stone_id = self.object.id
        return reverse_lazy("atik:detail-stone", kwargs={"pk": stone_id})
