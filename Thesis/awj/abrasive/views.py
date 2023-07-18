from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    FormView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from abrasive.forms import AbrasivesForm
from abrasive.models import (
    Abrasives,
    AbrasiveProperties,
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class HomeView(TemplateView):
    template_name = "abrasive/home.html"


class AddAbrasive(FormView):
    template_name = "abrasive/add-abrasive.html"
    form_class = AbrasivesForm
    fields = "__all__"

    def post(self, request):
        form = AbrasivesForm(request.POST)
        if form.is_valid():
            Abrasives.objects.create(
                name=form.cleaned_data.get("name"),
                chemical_properties=form.cleaned_data.get("chemical_properties"),
                sem_photo=form.cleaned_data.get("sem_photo"),
            )
            abrasive = Abrasives.objects.last()
            AbrasiveProperties.objects.create(
                abrasive=abrasive,
                density=form.cleaned_data.get("density"),
                hardness=form.cleaned_data.get("hardness"),
            )
            message = _("Abrasive Added Successfully")
            messages.success(request, message)
            return HttpResponseRedirect(reverse_lazy("abrasive:add-abrasive"))
        return AbrasivesForm()


class DeleteAbrasive(DeleteView):
    model = Abrasives
    success_url = reverse_lazy("abrasive:list-abrasive")

    def get(self, request):
        id = request.GET.get("id")
        return render(request, "list-abrasive", {"id": id})


class ListAbrasive(ListView):
    model = Abrasives
    template_name = "abrasive/list-abrasive.html"
    context_object_name = "abrasives"

    def get_context_data(self):
        context = super().get_context_data()
        context["abrasives"] = Abrasives.objects.all()
        return context


class DetailAbrasive(DetailView):
    model = Abrasives
    template_name = "abrasive/detail-abrasive.html"


class UpdateAbrasive(UpdateView):
    model = Abrasives
    template_name = "abrasive/update-abrasive.html"
    fields = "__all__"

    def get_success_url(self):
        abrasive_id = self.object.id
        return reverse_lazy("abrasive:detail-abrasive", kwargs={"pk": abrasive_id})


class UpdateAbrasiveProperties(UpdateView):
    model = AbrasiveProperties
    template_name = "abrasive/update-abrasive.html"
    fields = [
        "density",
        "hardness",
    ]

    def get_object(self, queryset=None):
        abrasive_id = self.kwargs["abrasive_id"]
        return self.model.objects.get(abrasive_id=abrasive_id)

    def get_success_url(self):
        abrasive_id = self.object.id
        return reverse_lazy("abrasive:detail-abrasive", kwargs={"pk": abrasive_id})
