from rest_framework import serializers
from .models import Brand, Car


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country', 'is_luxury']


class CarSerializer(serializers.ModelSerializer):
    brand_detail = BrandMinimalSerializer(source='brand', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'brand_name', 'brand_detail',
            'model_name', 'year', 'price', 'color',
            'fuel_type', 'mileage', 'is_available',
            'description', 'created_at',
        ]


class CarListSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'brand_name',
            'model_name', 'year', 'price',
            'color', 'fuel_type', 'is_available', 'created_at',
        ]