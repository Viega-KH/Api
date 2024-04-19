from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Sum
from django.core.paginator import Paginator
# from .models import HistoryEntry
from .models import Order
from .forms import Orderform





def IndxeViews(request):
    total_liters = Order.objects.aggregate(total_liters=Sum('liters'))
    objects = Order.objects.all()
    return render(request, 'block/dash.html', { 'total_liters':total_liters, 'object':objects } )




def TableViews(request):
    model = Order.objects.all().order_by('-id')
    paginator = Paginator(model, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = Orderform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table')
    else :
        form = Orderform()    


    return render(request, 'block/table.html', { 'list':page_obj, 'form':form })


def delete(request, id):
    data = get_object_or_404(Order, id=id)
    data.delete()
    return HttpResponseRedirect('/table')


# def edit(request, id):
#     date = get_object_or_404(Order, id=id)
#     if request.method == 'POST':
#         # Ma'lumotlar o'zgartirilgan formni qabul qilish
#         form = Orderform(request.POST, instance=date)
#         if form.is_valid():
#             form.save()  # O'zgartirilgan ma'lumotlarni saqlash
#             return redirect('order_list')  # Buyurtmalar ro'yxatiga qaytish
#     else:
#         # Boshqa holda, formni avvalgi buyurtmani bilan to'ldirish
#         form = Orderform(instance=date)
#     return render(request, 'block/table.html', {'form': form})  