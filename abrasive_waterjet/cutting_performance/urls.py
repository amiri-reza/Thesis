from django.urls import path
from cutting_performance.views import (
    HomeView,
    StonesAdd,
    AbrasivesAdd,
    CuttingDataAdd,
    StoneDetail,
    AbrasiveDetail,
    CuttingDataDetail,
    StoneUpdate,
    AbrasiveUpdate,
    CuttingDataUpdate,
    StoneDelete,
    AbrasiveDelete,
    CuttingDataDelete,



)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("stones/add/", StonesAdd.as_view(), name="stones-add"),
    path("abrasives/add/", AbrasivesAdd.as_view(), name="abrasives-add"),
    path("cutting-data/add/", CuttingDataAdd.as_view(), name="cutting-data-add"),
    path("stone/<int:pk>/", StoneDetail.as_view(), name="stone-detail"),
    path("abrasive/<int:pk>/", AbrasiveDetail.as_view(), name="abrasive-detail"),
    path("cutting-data/<int:pk>/", CuttingDataDetail.as_view(), name="cutting-data-detail"),
    path("stone/update/<int:pk>/", StoneUpdate.as_view(), name="stone-update"),
    path("abrasive/update/<int:pk>/", AbrasiveUpdate.as_view(), name="abrasive-update"),
    path("cutting-data/update/<int:pk>/", CuttingDataUpdate.as_view(), name="cutting-data-update"),
    path("stone/delete/<int:pk>/", StoneDelete.as_view(), name="stone-delete"),
    path("abrasive/delete/<int:pk>/", AbrasiveDelete.as_view(), name="abrasive-delete"),
    path("cutting-data/delete/<int:pk>/", CuttingDataDelete.as_view(), name="cutting-data-delete"),
]