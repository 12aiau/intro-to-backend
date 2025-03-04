from django.urls import path
from .views import table_list, create_table

urlpatterns = [
    path("tables/", table_list),
    path("tables/create/", create_table),
]
