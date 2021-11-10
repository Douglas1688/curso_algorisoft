from django.urls import path
from erp.vistas.views import *

app_name = 'erp'

urlpatterns = [
    path('category/',CategoryListView.as_view(),name='vista1'),
]