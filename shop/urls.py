from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Shop.Index"),
    path('about/', views.about, name="Shop.about"),
    path('contact/', views.contact, name="Shop.contact"),
    path('search/', views.search, name="Shop.search"),
    path('checkout/', views.checkout, name="Shop.checkout"),
    path('tracker/', views.tracker, name="Shop.tracker"),
    path('products/<int:qvid>', views.products, name="Shop.products"),
]
