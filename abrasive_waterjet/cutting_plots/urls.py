from django.urls import path
from cutting_plots.views import plotter, plot_selector

app_name = "cutting_plots"
urlpatterns = [
    path("plotter/<str:parameter>/", plotter, name="plotter"),
    path("main/", plot_selector, name="plot_selector"),

]