from django.db import models

# Create your models here.
class Accounts_receivable(models.Model):
    day = models.DateField('出库日期', )
    FBillNo2 = models.TextField('千方单据号')
    word = models.TextField('产品长代码')

    name_1 = models.CharField('产品名称', max_length=300, )
    ITEM = models.CharField('规格型号', max_length=300, )
    unit = models.CharField('单位', max_length=30, )
    batch_number = models.TextField('批号')
    number_1 = models.DecimalField('销售数量', max_digits=10,
                                   decimal_places=2,
                                   default=0.0
                                   )
    price_1 = models.DecimalField('销售单价', max_digits=7,
                                  decimal_places=2,
                                  default=0.0
                                  )
    money_1 = models.DecimalField('销售金额', max_digits=10,
                                  decimal_places=2,
                                  default=0.0
                                  )
    Purchase = models.CharField('购货单位', max_length=50, default='')
    administrative_office=models.CharField('科室',max_length=50,default='')
    tax_rate_a=models.DecimalField('税率', max_digits=4,
                                  decimal_places=2,
                                  default=0.0
                                  )
    salesman = models.CharField('业务员', max_length=30, default='')
    area_a = models.IntegerField('区域')
    remark_a=models.CharField('备注', max_length=50, default='')
    put_away=models.CharField('收单情况', max_length=50, default='')
    fapiao_day = models.DateField('开票日期', )
    fapiao_number=models.IntegerField('发票号码')
    put_money_date=models.DateField('回款日期', )
    put_money_number=models.TextField('回款银行编号')
    put_money_1=models.DecimalField('回款金额', max_digits=15,
                                  decimal_places=2,
                                  default=0.0,)
    type_1=models.CharField('类型（试剂或设备）', max_length=50, default='')

