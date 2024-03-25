from django.urls import path
from .views import new_joby


app_name = "jobys"

urlpatterns = [
    path("new-joby/", new_joby, name="new_joby"),
]
