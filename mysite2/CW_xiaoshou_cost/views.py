
from django.http import HttpResponse
from django.shortcuts import render
from docutils.nodes import row

from CW_xiaoshou_cost import models
import csv

from mysite2 import settings
from .models import make_money
import os
import xlrd



# Create your views here.
def test_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="test.csv"'
    # all_data = ['a', 'b', 'c', 'd']
    all_data =models.make_money.objects.all()
    writer = csv.writer(response)
    writer.writerow(['id','salesman','Purchase','administrative_office','day','FBillNo1','FBillNo2','VAR','word','name_1','ITEM','unit','batch_number','number_1','price_1','money_1','haulage_1','unit_cost','Proportion_1','remark_1','tax_rate_1','cost_A','cost_B','Margin_A','Margin_B','Tax_rate_2','Push_money'])
    for b in all_data:
        writer.writerow([b.id, b.salesman, b.Purchase, b.administrative_office, b.day, b.FBillNo1, b.FBillNo2,
             b.VAR, b.word, b.name_1, b.ITEM, b.unit, b.batch_number, b.number_1, b.price_1,
             b.money_1, b.haulage_1, b.unit_cost, b.Proportion_1, b.remark_1, b.tax_rate_1, b.cost_A,
             b.cost_B, b.Margin_A, b.Margin_B, b.Tax_rate_2, b.Push_money])
    return response




###day08
def test_upload(request):

    if request.method == 'GET':
        return render(request, 'cost/test_upload.html')
    elif request.method == 'POST':
        title= request.POST['title']
        c = request.FILES['myfile']
        # f = c.name
        b = open('c','r')

        for i in b:

            print(i)

        # make_money.objects.create(salesman=i.salesman,Purchase=i.Purchase,administrative_office=i.administrative_office,day=i.day,FBillNo1=i.FBillNo1,FBillNo2=i.FBillNo2,VAR=i.VAR,word=i.word,name_1=i.name_1,ITEM=i.ITEM,unit=i.unit,batch_number=i.batch_number,number_1=i.number_1,price_1=i.price_1,money_1=i.money_1,haulage_1=i.haulage_1,unit_cost=i.unit_cost,Proportion_1=i.Proportion_1,remark_1=i.remark_1,tax_rate_1=i.tax_rate_1,cost_A=i.cost_A,cost_B=i.cost_B,Margin_A=i.Margin_A,Margin_B=i.Margin_B,Tax_rate_2=i.Tax_rate_2,Push_money=i.Push_money)

        return HttpResponse('--上传文件成功--')

def all_cost(request):
    all_cost=models.make_money.objects.all()
    return render(request, 'cost/销售明细成本报表页面.html',locals())


def upload_view(request):
    if request.method == 'GET' :
        return render(request,'cost/test_upload1.html')
    elif request.method =='POST':
        a_file =request.FILES['myfile']
        print("上传的文件名是：",a_file.name)
        filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as f:
            data = a_file.file.read()
            f.write(data)
            # data_a = data.decode()
            data = xlrd.open_workbook(filename)
            table = data.sheets()[0]
            nrows = table.nrows
            for m in nrows-2:
                m_a =table.row(m+2)
                make_money.objects.create(salesman=m_a[0], Purchase=m_a[1],
                                          administrative_office=m_a[2], day=m_a[3], FBillNo1=m_a[4],
                                          FBillNo2=m_a[5], VAR=m_a[6], word=m_a[7], name_1=m_a[8], ITEM=m_a[9],
                                          unit=m_a[10], batch_number=m_a[11], number_1=m_a[12],
                                          price_1=m_a[13], money_1=m_a[14], haulage_1=m_a[15],
                                          unit_cost=m_a[16], Proportion_1=m_a[17], remark_1=m_a[18],
                                          tax_rate_1=m_a[19], cost_A=m_a[20], cost_B=m_a[21],
                                          Margin_A=m_a[22], Margin_B=m_a[23], Tax_rate_2=m_a[24],
                                          Push_money=m_a[25])




        return HttpResponse("接收文件："+ a_file.name + "成功")




