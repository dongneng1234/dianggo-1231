from django.db import models

# Create your models here.
class haulage_HL(models.Model):
    day = models.DateField('日期', )
    salesman = models.CharField('业务员', max_length=30, default='')
    Purchase = models.CharField('客户', max_length=50, default='')
    haulage_HL_people = models.DecimalField('运费', max_digits=10,
                                  decimal_places=2,
                                  default=0.0)
    remark_1 = models.CharField('备注', max_length=50, default='')

