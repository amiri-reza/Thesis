from django.views.generic import TemplateView
from cutting_performance.views import CuttingData, Abrasive, NaturalStone
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Users




class MainPage(TemplateView):
    template_name = "home/index.html"

    

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "home/dashboard.html"
    def get_context_data(self):
        context = super().get_context_data()
        
        context["user"] = Users.objects.get(id = self.request.user.id)
        #breakpoint()
        context["stones"] = NaturalStone.objects.all()
        context["stones_num"] = NaturalStone.objects.count()
        context["abrasives"] = Abrasive.objects.all()
        context["abrasives_num"] = Abrasive.objects.count()
        context["cutting_data"] = CuttingData.objects.all()
        context["cut_num"] = CuttingData.objects.count()
        context["plots_num"] = NaturalStone.objects.count()
        return context


