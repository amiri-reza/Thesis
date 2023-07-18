from django.urls import path
from cutting.views import CuttingView

app_name = "cutting"

urlpatterns = [
    path("result/", CuttingView.as_view(), name="result"),
]
