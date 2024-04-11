from django.urls import path
from .views import TableViews, IndxeViews

urlpatterns = [
    path( '', IndxeViews, name='index' ),
    path( 'info', TableViews, name='table' ),
]
