from django.urls import path
from plots.views import plotting, corr_plotter

app_name = "plots"
urlpatterns = [
    path("bar_chart/<str:plot>/", plotting, name="plots"),
    path("correlation_plot/", corr_plotter, name="corr"),
]
