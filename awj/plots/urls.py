from django.urls import path
from plots.views import plotting, corr_plotter, max_min_cutting_depth_corr

app_name = "plots"
urlpatterns = [
    path("bar_chart/<str:plot>/", plotting, name="plots"),
    path("correlation_plot/", corr_plotter, name="corr"),
    path("cut-max-min-corr/", max_min_cutting_depth_corr, name="cut-max-min-corr"),
]
