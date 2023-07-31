from django.db import models

# Create your models here.

class Signature(models.Model):
    numberInput = models.IntegerField('Номер Входящий',null=True,blank=True)
    user = models.CharField('Подпись пользователя',blank=True,null=True,max_length=2000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)


class InputJournal(models.Model):

    signature = models.ForeignKey(Signature,on_delete=models.CASCADE,null=True, blank=True)
    dateReg = models.DateField('Дата регисрации',null=True,blank=True)
    numberInput = models.IntegerField('Номер Входящий',null=True,blank=True)
    correspondent = models.CharField('Кореспондент (откуда поступило)',null=True,blank=True,max_length=10000)
    content = models.CharField('Краткое содержание',null=True,blank=True,max_length=10000)
    datenumber = models.CharField('Дата и исходящий номер',null=True,blank=True,max_length=1000)
    executor = models.CharField('Исполнитель',null=True,blank=True,max_length=10000)
    executionDate = models.DateField('Сроки исполнения',null=True,blank=True,max_length=1000)
    mark = models.CharField('Отметка об исполнении', null=True, blank=True, max_length=1000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)
    dateTimeReg = models.DateTimeField('Дата и время регисрации',null=True,blank=True)#auto_now_add=True


