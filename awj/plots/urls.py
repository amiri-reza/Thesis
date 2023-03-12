from django.urls import path
from plots.views import plotting

app_name = "plots"
urlpatterns = [
    path("<str:plot>/", plotting, name="plots"),
]
