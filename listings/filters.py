import django_filters 
from listings.models import Listing

class listingFilters(django_filters.FilterSet):
    address= django_filters.CharFilter(lookup_expr='icontains')
    CHOICES=(
        ('ascending', 'Ascending'),
        ('decending', 'Descending')
    )
   
    # ordering=django_filters.ChoiceFilter(label='Ordering' ,choices=CHOICES, method='filter_by_order')
    class Meta:
        model=Listing
        fields=['price', 'bedrooms', 'bathromms', 'city', 'region', 'address']
    def filter_by_order(self,queryset, name, value):
        expression='created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)
