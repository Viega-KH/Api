from django.shortcuts import render
from .models import Order





def TableViews(request):
    model = Order.objects.all()
    return render(request, 'block/table.html', { 'list':model })
