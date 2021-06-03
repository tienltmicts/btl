from django.shortcuts import render, get_object_or_404

from .models import *

from .forms import *
import datetime

# Create your views here.
def statistical(request):
    filters = ['Tồn', 'Tồn nhiều nhất', 'Bán chạy nhất', 'Bán chạy']
    query_string = ''
    times = [(1,'Tháng 1'),(2,'Tháng 2') ,(3, 'Tháng 3') , (4,'Tháng 4'), (5, 'Tháng 5'), (6, 'Tháng 6'), (7, 'Tháng 7'), (8, 'Tháng 8'),(9,'Tháng 9') , (10, 'Tháng 10'),(11, 'Tháng 11'),(12, 'Tháng 12'), (13, 'Năm trước')]
    produces = []
    time=''
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            query_string = request.GET['param']
            time = int(request.GET['times'])
            
            if time == 13:
                if query_string == 'Tồn':
                    produce = Produces.objects.filter(added_date__year__lt = datetime.datetime.now().year).order_by('-inventory')
                    for i in produce:
                        produces.append(i)
                elif query_string == 'Tồn nhiều nhất':
                    produces.append(Produces.objects.filter(added_date__year__lt = datetime.datetime.now().year).latest('inventory'))
                elif query_string == 'Bán chạy nhất':
                    produces.append(Produces.objects.filter(added_date__year__lt = datetime.datetime.now().year).latest('sold'))
                else:
                    produce = Produces.objects.filter(added_date__year__lt = datetime.datetime.now().year).order_by('-sold')
                    for i in produce:
                        produces.append(i)
            else: 
                if query_string == 'Tồn':
                    produce = Produces.objects.filter(added_date__year = datetime.datetime.now().year,added_date__month=time ).order_by('-inventory')
                    for i in produce:
                        produces.append(i)
                elif query_string == 'Tồn nhiều nhất':
                    produces.append(Produces.objects.filter(added_date__year = datetime.datetime.now().year,added_date__month=time).latest('inventory'))
                elif query_string == 'Bán chạy nhất':
                    produces.append(Produces.objects.filter(added_date__year = datetime.datetime.now().year,added_date__month=time).latest('sold'))
                else:
                    produce = Produces.objects.filter(added_date__year = datetime.datetime.now().year,added_date__month=time).order_by('-sold')
                    for i in produce:
                        produces.append(i)
    else:
        form = FilterForm()
    
    return render(request, "admin/statistical.html", {
        'form': form,
        'filters': filters,
        'query_string': query_string,
        'times': times,
        'time': time,
        'produces': produces
    })