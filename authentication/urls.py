from django.urls import path

from .views import login_view

urlpatterns = [
    path('login/', login_view, name="login"),
    # path('register/', RegisterView.as_view(), name="register"),
    # path('logout', LogoutView.as_view(), name="logout")
]

app_name = "authentication"