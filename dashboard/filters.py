import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class ProductFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateFilter(field_name='created_at', lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = CharFilter(field_name='category', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product', 'created_at']