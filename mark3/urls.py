from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', api_views.storeList.as_view()),
]
