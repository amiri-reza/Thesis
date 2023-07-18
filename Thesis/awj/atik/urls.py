from django.urls import path
from atik.views import (
    HomeView,
    AddNaturalStone,
    ListNaturalStone,
    UpdateNaturalStone,
    UpdatePhysicalProperties,
    UpdateMechanicalProperties,
    DetailNaturalStone,
    DeleteNaturalStone,
)


app_name = "atik"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-stone/", AddNaturalStone.as_view(), name="add-stone"),
    path("list-stone/", ListNaturalStone.as_view(), name="list-stone"),
    path("update-stone/<int:pk>/", UpdateNaturalStone.as_view(), name="update-stone"),
    path(
        "update-mechanical/<int:stone_id>/",
        UpdateMechanicalProperties.as_view(),
        name="update-mechanical",
    ),
    path(
        "update-physical/<int:stone_id>/",
        UpdatePhysicalProperties.as_view(),
        name="update-physical",
    ),
    path("detail-stone/<int:pk>/", DetailNaturalStone.as_view(), name="detail-stone"),
    path("delete-stone/<int:pk>/", DeleteNaturalStone.as_view(), name="delete-stone"),
]
