from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination

from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer, CarListSerializer


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'country', 'founded_year']
    ordering = ['name']

    def get_queryset(self):
        if self.action == 'list':
            return (
                Brand.objects
                .prefetch_related('cars')
                .only('id', 'name', 'country', 'founded_year', 'is_luxury')
            )
        return Brand.objects.prefetch_related('cars').all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class CarViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['model_name', 'color', 'fuel_type', 'brand__name']
    ordering_fields = ['price', 'year', 'mileage', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        base_qs = Car.objects.select_related('brand')
        if self.action == 'list':
            return (
                base_qs
                .defer('description')
                .only(
                    'id', 'brand', 'model_name', 'year', 'price', 'color',
                    'fuel_type', 'is_available', 'created_at',
                    'brand__id', 'brand__name',
                )
            )
        return (
            base_qs
            .only(
                'id', 'brand', 'model_name', 'year', 'price', 'color',
                'fuel_type', 'mileage', 'is_available', 'description', 'created_at',
                'brand__id', 'brand__name', 'brand__country', 'brand__is_luxury',
            )
        )

    def get_serializer_class(self):
        if self.action == 'list':
            return CarListSerializer
        return CarSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAdminUser()]