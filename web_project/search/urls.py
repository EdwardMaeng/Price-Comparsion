from django.urls import path
from search import views

urlpatterns = [
    path("", views.search, name=""),
    path("result/<product>", views.result, name="result")
]