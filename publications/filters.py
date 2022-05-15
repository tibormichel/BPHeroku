import django_filters


from people import models
from publications.models import Publication
from people.models import Person


class PublicationFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    # created_by = django_filters.ChoiceFilter()
    # content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Publication
        fields = ('title','created_by')
        # fields = {
        #     'title': ['icontains'],
        #     'created_by' : []
        #
        # }

        # fields += ('title','created_by')