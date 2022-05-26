import django_filters


from publications.models import Publication


class PublicationFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Publication
        fields = ('title','created_by')
