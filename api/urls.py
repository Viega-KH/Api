from django.urls import path
from .views import TableViews, IndxeViews, delete

urlpatterns = [
    path( '', IndxeViews, name='index' ),
    path( 'table', TableViews, name='table' ),
    path( 'info/<int:id>', delete, name='delete' ),
]
