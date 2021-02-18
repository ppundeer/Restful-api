from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views as api_views
from restapi.APIs.views import StatList, queryList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plot1/', queryList.as_view()),
    path('segment/', StatList.as_view()),
]
