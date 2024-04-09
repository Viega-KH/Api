from django.urls import path
from .views import TableViews

urlpatterns = [
    path( 'info', TableViews, name='table' )
]
