from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import Orderform




def IndxeViews(request):
    return render(request, 'block/dash.html')




def TableViews(request):
    model = Order.objects.all()
    if request.method == 'POST':
        form = Orderform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else :
        form = Orderform()    


    return render(request, 'block/table.html', { 'list':model, 'form':form })

