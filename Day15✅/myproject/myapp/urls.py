from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),    # corrected this
    path('logout/', logout_view, name="logout"),  # corrected this
]
