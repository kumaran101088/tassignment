import pandas, datetime
from .models import Inventory
from django.contrib import messages
from django.http import HttpResponse
from .filters import InventoryFilter
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def home_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_name =  str(request.FILES.get('file')).strip()
        is_csv = file_name.endswith('.csv')
        if is_csv:
            df = pandas.read_csv(file)
            data_to_be_loaded = []
            start_time = datetime.datetime.now().replace(microsecond=0)
            for row, _ in df.iterrows():
                data_to_be_loaded.append(Inventory(
                    store=df.loc[row, 'store'],
                    sku=df.loc[row, 'sku'],
                    product=df.loc[row, 'product'],
                    price=df.loc[row, 'price'],
                    date=df.loc[row, 'date'],
                ))
            Inventory.objects.bulk_create(data_to_be_loaded)
            end_time = datetime.datetime.now().replace(microsecond=0)
            print(f'Total time: {end_time - start_time}')
        else:
            messages.error(request, 'file must have a .csv extension')
        return redirect('home')
    elif request.method == 'GET':
        products = Inventory.objects.all().order_by('-id')
        filter = InventoryFilter(request.GET, queryset=products)
        paginator = Paginator(filter.qs, 5)
        page = request.GET.get('page')
        try:
            page_object = paginator.get_page(page)
        except:
            page_object = paginator.get_page(1)
        context = {
            'page_object' : page_object,
            'filter' : filter
        }
        return render(request, 'app/home.html', context=context)