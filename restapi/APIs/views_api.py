from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from restapi.models import superstore
from .serializers import SegSerializer, CatSerializer, SubSerializer, RegSerializer, \
                         OrderSerializer, StateSerializer, CitySerializer
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear

class typeList(ListAPIView):
    queryset = ''
    def list(self, request):
        query1 = superstore.objects.annotate(year=ExtractYear('order_date')).values('segment', 'year')\
            .annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer1 = SegSerializer(list(query1), many=True)
        query2 = superstore.objects.annotate(year=ExtractYear('order_date')).values('category', 'year')\
            .annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer2 = CatSerializer(list(query2), many=True)
        query3 = superstore.objects.annotate(year=ExtractYear('order_date')).values('sub_category', 'year')\
            .annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer3 = SubSerializer(list(query3), many=True)
        query4 = superstore.objects.annotate(year=ExtractYear('order_date')).values('region', 'year')\
            .annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer4 = RegSerializer(list(query4), many=True)

        result = {"segment": {2014: serializer1.data[0:3],
                              2015: serializer1.data[3:6],
                              2016: serializer1.data[6:9],
                              2017: serializer1.data[9:]},
                  "category": {2014: serializer2.data[0:3],
                               2015: serializer2.data[3:6],
                               2016: serializer2.data[6:9],
                               2017: serializer2.data[9:]},
                  "sub_category": {2014: serializer3.data[0:17],
                                   2015: serializer3.data[17:34],
                                   2016: serializer3.data[34:51],
                                   2017: serializer3.data[51:]},
                  "region": {2014: serializer4.data[0:4],
                             2015: serializer4.data[4:8],
                             2016: serializer4.data[8:12],
                             2017: serializer4.data[12:]}
                  }
        return Response(result)

class orderList(ListAPIView):
    queryset = ''
    def list(self, request):
        query1 = superstore.objects.annotate(year=ExtractYear('order_date')).annotate(month=ExtractMonth('order_date'))\
            .values('year', 'month').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year', 'month')
        serializer = OrderSerializer(list(query1), many=True)

        result = {2014: serializer.data[0:12],
                  2015: serializer.data[12:24],
                  2016: serializer.data[24:36],
                  2017: serializer.data[36:]}
        return Response(result)

class stateList(ListAPIView):
    queryset = ''
    def list(self, request):
        query1 = superstore.objects.filter(order_date__year=2014).annotate(year=ExtractYear('order_date'))\
            .values('state', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer1 = StateSerializer(list(query1), many=True)

        query2 = superstore.objects.filter(order_date__year=2015).annotate(year=ExtractYear('order_date')) \
            .values('state', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer2 = StateSerializer(list(query2), many=True)

        query3 = superstore.objects.filter(order_date__year=2016).annotate(year=ExtractYear('order_date')) \
            .values('state', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer3 = StateSerializer(list(query3), many=True)

        query4 = superstore.objects.filter(order_date__year=2017).annotate(year=ExtractYear('order_date')) \
            .values('state', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer4 = StateSerializer(list(query4), many=True)

        result = {2014: serializer1.data,
                  2015: serializer2.data,
                  2016: serializer3.data,
                  2017: serializer4.data}
        return Response(result)

class cityList(ListAPIView):
    queryset = ''
    def list(self, request):
        query1 = superstore.objects.filter(order_date__year=2014).annotate(year=ExtractYear('order_date')) \
            .values('city', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer1 = CitySerializer(list(query1), many=True)

        query2 = superstore.objects.filter(order_date__year=2015).annotate(year=ExtractYear('order_date')) \
            .values('city', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer2 = CitySerializer(list(query2), many=True)

        query3 = superstore.objects.filter(order_date__year=2016).annotate(year=ExtractYear('order_date')) \
            .values('city', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer3 = CitySerializer(list(query3), many=True)

        query4 = superstore.objects.filter(order_date__year=2017).annotate(year=ExtractYear('order_date')) \
            .values('city', 'year').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('year')
        serializer4 = CitySerializer(list(query4), many=True)

        result = {2014: serializer1.data,
                  2015: serializer2.data,
                  2016: serializer3.data,
                  2017: serializer4.data}
        return Response(result)
