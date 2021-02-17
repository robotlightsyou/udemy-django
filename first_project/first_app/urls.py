from django.urls import path
from first_app import views



urlpatterns = [
    path("", views.index, name='index'),
    path("help", views.help, name='help'),
    path("users", views.users, name='users'),
    # path("forms", views.form_name_view, name='forms'),
]
