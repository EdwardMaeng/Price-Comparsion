from django.urls import path
from search import views
urlpatterns = [
    path("search", views.hello_there, name="hello_there"),
]