from django.urls import path
from . import views
from . views import dashboard, create_short_url, redirect_url

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_short_url, name='create'),
    path('<str:code>/', redirect_url, name='redirect'),
    path("delete/<int:id>/", views.delete_url, name="delete"),
]
