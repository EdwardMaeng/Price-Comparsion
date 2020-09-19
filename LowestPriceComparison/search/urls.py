from django.urls import path
from LowestPricePredicter.Search import views

urlpatterns = [
    path("", views.home, name="home"),
]