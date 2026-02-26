from django.urls import path
from .views import BrandListCreateView, BrandDetailView, CarListCreateView, CarDetailView

urlpatterns = [
    path('brands/', BrandListCreateView.as_view()),
    path('brands/<int:pk>/', BrandDetailView.as_view()),
    path('cars/', CarListCreateView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()),
]