from django.urls import path

from second import views

urlpatterns = [
    path('list/', views.list, name="list"),
]

