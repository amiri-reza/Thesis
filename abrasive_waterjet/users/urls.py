from django.urls import path

from users.views import SignUp, SignIn, SignOut, DeleteUser, DetailUser, UpdateUser

app_name = "users"
urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),
    path("signout/", SignOut.as_view(), name="signout"),
    path("delete/<int:pk>/", DeleteUser.as_view(), name="delete"),
    path("detail/<int:pk>/", DetailUser.as_view(), name="detail"),
    path("update/<int:pk>/", UpdateUser.as_view(), name="update"),
]


