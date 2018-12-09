from django.db import models
from company.models import Company


class Account(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='accounts', verbose_name="Компания")
	bank = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование банка")
	bik = models.CharField(max_length=9, null=False, blank=False, verbose_name="БИК")
	kor = models.CharField(max_length=20, null=False, blank=False, verbose_name="Кор. счет")
	number = models.CharField(max_length=20, null=False, blank=False, verbose_name="Расчетный счет")
	default = models.BooleanField(default=False, verbose_name="Основной счет")

	def __str__(self):
		return '{} ({})'.format(self.company.name, self.bank, self.number)

	class Meta:
		verbose_name = u'Банковский счет'
		verbose_name_plural = u'Банковские счета'