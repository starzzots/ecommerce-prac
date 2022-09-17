from django.urls import path
from . import views

urlpatterns = [
    path("store/", views.store),
    path("cart/", views.cart),
    path("main/", views.main),
    path("checkout/", views.checkout),
]
