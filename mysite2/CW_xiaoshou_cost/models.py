from django.db import models

# Create your models here.
class make_money(models.Model):
    salesman =models.CharField('业务员',max_length=30,default='')
    Purchase =models.CharField('购货单位',max_length=50,default='')
    administrative_office = models.CharField('科室', max_length=50, default='')
    day =models.DateField('出库日期',)
    FBillNo1=models.TextField('金蝶单据号')
    FBillNo2=models.TextField('千方单据号')
    VAR =models.CharField('品种',max_length=50,)
    word =models.TextField('产品长代码')
    name_1 =models.CharField('产品名称',max_length=300,)
    ITEM =models.CharField ('规格型号',max_length=300,)
    unit =models.CharField('单位',max_length=30,)
    batch_number =models.TextField('批号')
    number_1 =models.DecimalField('销售数量',max_digits=10,
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
    haulage_1=models.DecimalField('托运费', max_digits=7,
                                   decimal_places=2,
                                   default=0.0
                                   )
    unit_cost=models.DecimalField('单位成本', max_digits=7,
                                   decimal_places=2,
                                   default=0.0
                                   )
    Proportion_1=models.DecimalField('比例', max_digits=4,
                                   decimal_places=2,
                                   default=0.0
                                   )
    remark_1 = models.CharField('备注', max_length=50, default='')

    tax_rate_1 = models.DecimalField('税率', max_digits=4,
                                   decimal_places=2,
                                   default=0.0
                                   )
    cost_A= models.DecimalField('成本A', max_digits=10,
                                   decimal_places=2,
                                   default=0.0
                                   )
    cost_B = models.DecimalField('成本B', max_digits=10,
                                 decimal_places=2,
                                 default=0.0
                                 )
    Margin_A = models.DecimalField('毛利A', max_digits=10,
                                 decimal_places=2,
                                 default=0.0
                                 )
    Margin_B = models.DecimalField('毛利B', max_digits=10,
                                 decimal_places=2,
                                 default=0.0
                                 )
    Tax_rate_2 = models.DecimalField('企业所得税额', max_digits=10,
                                   decimal_places=2,
                                   default=0.0
                                   )
    Push_money = models.DecimalField('提成', max_digits=10,
                                   decimal_places=2,
                                   default=0.0
                                   )
    class Meta:
        db_table = 'make_money'

    def __str__(self):
        return '%s_%s_%s_%s%_s_%s_%s_%s_%s_%s_%s%_s_%s_%s_%s_%s_%s%_s_%s_%s__%s_%s_%s%_s_%s_%s_%s_%s_%s_%s%_s_%s_%s_%s_%s_%s%_s_%s_%s'