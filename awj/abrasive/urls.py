from django.urls import path
from abrasive.views import (
    HomeView,
    AddAbrasive,
    ListAbrasive,
    UpdateAbrasive,
    UpdateAbrasiveProperties,
    DetailAbrasive,
    DeleteAbrasive,
)


app_name = "abrasive"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-abrasive/", AddAbrasive.as_view(), name="add-abrasive"),
    path("list-abrasive/", ListAbrasive.as_view(), name="list-abrasive"),
    path("update-abrasive/<int:pk>/", UpdateAbrasive.as_view(), name="update-abrasive"),
    path(
        "update-properties/<int:abrasive_id>/",
        UpdateAbrasiveProperties.as_view(),
        name="update-properties",
    ),
    path("detail-abrasive/<int:pk>/", DetailAbrasive.as_view(), name="detail-abrasive"),
    path("delete-abrasive/<int:pk>/", DeleteAbrasive.as_view(), name="delete-abrasive"),
]
