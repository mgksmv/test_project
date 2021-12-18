from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TableListView.as_view(), name='index'),
    path('filter/', views.filter_data, name='filter'),
    path('reset/', views.reset_filter, name='reset'),
]
