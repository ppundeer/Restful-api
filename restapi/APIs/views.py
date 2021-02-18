from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from restapi.models import superstore
from .serializers import StatSerializer
from django.db.models import Sum
from django.db.models.functions import ExtractMonth

class StatList(ListAPIView):
    serializer_class = StatSerializer
    queryset = superstore.objects.filter(order_date__year=2015).values('segment').annotate(sales=Sum('sales'), profit=Sum('profit'))
    def list(self, request):
        query = self.get_queryset()
        serializer = StatSerializer(list(query), many=True)
        return Response(serializer.data)

class queryList1(APIView):

    def get(self, request):
        query_s1 = superstore.objects.filter(order_date__year=2014).values('segment').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_s2 = superstore.objects.filter(order_date__year=2015).values('segment').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_s3 = superstore.objects.filter(order_date__year=2016).values('segment').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_s4 = superstore.objects.filter(order_date__year=2017).values('segment').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_c1 = superstore.objects.filter(order_date__year=2014).values('category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_c2 = superstore.objects.filter(order_date__year=2015).values('category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_c3 = superstore.objects.filter(order_date__year=2016).values('category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_c4 = superstore.objects.filter(order_date__year=2017).values('category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_b1 = superstore.objects.filter(order_date__year=2014).values('sub_category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_b2 = superstore.objects.filter(order_date__year=2015).values('sub_category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_b3 = superstore.objects.filter(order_date__year=2016).values('sub_category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_b4 = superstore.objects.filter(order_date__year=2017).values('sub_category').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_r1 = superstore.objects.filter(order_date__year=2014).values('region').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_r2 = superstore.objects.filter(order_date__year=2015).values('region').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_r3 = superstore.objects.filter(order_date__year=2016).values('region').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_r4 = superstore.objects.filter(order_date__year=2017).values('region').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))

        return JsonResponse({"segment": {2014: list(query_s1), 2015: list(query_s2),
                                         2016: list(query_s3), 2017: list(query_s4)},
                             "category": {2014: list(query_c1), 2015: list(query_c2),
                                          2016: list(query_c3), 2017: list(query_c4)},
                             "sub-category": {2014: list(query_b1), 2015: list(query_b2),
                                              2016: list(query_b3), 2017: list(query_b4)},
                             "region": {2014: list(query_r1), 2015: list(query_r2),
                                        2016: list(query_r3), 2017: list(query_r4)}
                             })

class queryList2(APIView):
    def get(self, request):

        query_1 = superstore.objects.filter(order_date__year=2014).annotate(month=ExtractMonth('order_date'))\
                .values('month').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('month')
        query_2 = superstore.objects.filter(order_date__year=2015).annotate(month=ExtractMonth('order_date'))\
                .values('month').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('month')
        query_3 = superstore.objects.filter(order_date__year=2016).annotate(month=ExtractMonth('order_date'))\
                .values('month').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('month')
        query_4 = superstore.objects.filter(order_date__year=2017).annotate(month=ExtractMonth('order_date'))\
                .values('month').annotate(sales=Sum('sales'), profit=Sum('profit')).order_by('month')

        return JsonResponse({2014: list(query_1), 2015: list(query_2), 2016: list(query_3), 2017: list(query_4)})


class queryList3(APIView):
    def get(self, request):

        query_1 = superstore.objects.filter(order_date__year=2014).values('state').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_2 = superstore.objects.filter(order_date__year=2015).values('state').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_3 = superstore.objects.filter(order_date__year=2016).values('state').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_4 = superstore.objects.filter(order_date__year=2017).values('state').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))

        return JsonResponse({2014: list(query_1), 2015: list(query_2), 2016: list(query_3), 2017: list(query_4)})


class queryList4(APIView):
    def get(self, request):

        query_1 = superstore.objects.filter(order_date__year=2014).values('city').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_2 = superstore.objects.filter(order_date__year=2015).values('city').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_3 = superstore.objects.filter(order_date__year=2016).values('city').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))
        query_4 = superstore.objects.filter(order_date__year=2017).values('city').annotate(sales=Sum('sales'),
                                                                                            profit=Sum('profit'))

        return JsonResponse({2014: list(query_1), 2015: list(query_2), 2016: list(query_3), 2017: list(query_4)})
