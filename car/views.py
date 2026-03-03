from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'country', 'founded_year']
    ordering = ['name']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related('brand').all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['model_name', 'color', 'fuel_type', 'brand__name']
    ordering_fields = ['price', 'year', 'mileage', 'created_at']
    ordering = ['-created_at']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminUser()]
    