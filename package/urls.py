

from django.contrib import admin
from django.urls import path
from package import views


admin.site.site_header = "Package Management Suite"
urlpatterns = [
    path('', views.main_page)
    ]