from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views as api_views
from restapi.APIs.views import queryList1, queryList2, queryList3, queryList4
from restapi.APIs.views_api import typeList, orderList, stateList, cityList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plot1/', queryList1.as_view()),
    path('plot2/', queryList2.as_view()),
    path('plot3/', queryList3.as_view()),
    path('plot4/', queryList4.as_view()),
    path('type/', typeList.as_view()),
    path('order/', orderList.as_view()),
    path('state/', stateList.as_view()),
    path('city/', cityList.as_view()),
]
