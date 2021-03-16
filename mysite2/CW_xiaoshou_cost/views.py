import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import csv
from CW_xiaoshou_cost.models import make_money



# Create your views here.
def test_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="test.csv"'
    all_data = ['a', 'b', 'c', 'd']
    writer = csv.writer(response)
    writer.writerow(all_data)
    return response



####day08
def test_upload(request):

    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        salesman = request.POST['title']
        #Purchase = request.FILES['myfile']

        # make_money.objects.create(salesman=salesman, Purchase=Purchase)

        return HttpResponse('--上传文件成功--')

def page_1(request):
    return HttpResponse("woshoghowehivnigh ")
