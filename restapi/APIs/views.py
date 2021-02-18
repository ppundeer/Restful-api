from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from restapi.models import superstore
from .serializers import StatSerializer
from django.db.models import Sum

class StatList(ListAPIView):
    serializer_class = StatSerializer
    queryset = superstore.objects.filter(order_date__year=2015).values('segment').annotate(sales=Sum('sales'), profit=Sum('profit'))
    def list(self, request):
        query = self.get_queryset()
        serializer = StatSerializer(list(query), many=True)
        return Response(serializer.data)

class queryList(APIView):
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

        return JsonResponse({"segment_2014": list(query_s1), "segment_2015": list(query_s2),
                             "segment_2016": list(query_s3), "segment_2017": list(query_s4),
                             "category_2014": list(query_c1), "category_2015": list(query_c2),
                             "category_2016": list(query_c3), "category_2017": list(query_c4),
                             "subcatg_2014": list(query_b1), "subcatg_2015": list(query_b2),
                             "subcatg_2016": list(query_b3), "subcatg_2017": list(query_b4),
                             "region_2014": list(query_r1), "region_2015": list(query_r2),
                             "region_2016": list(query_r3), "region_2017": list(query_r4)
                             })

