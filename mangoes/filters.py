from .models import Mango_For_Sell
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Mango_For_Sell
        fields = ['owner', 'Type_Of_Mango',"ripe","pkgd_at","price","discount"]
        # fields={
        #     'owner': ['exact', ],
        #     "Type_Of_Mango":['exact'],
        #     'ripe': ['icontains', ],
        #     'pkgd_at': ['year', 'year__gt', 'year__lt','month', 'month__gt', 'month__lt' ,'day', 'day__gt', 'day__lt'],
        #     'price':['lt','exact',],
        #     "discount":['exact','gt']
        # }

        