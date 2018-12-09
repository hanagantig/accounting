from django.db import models
from company.models import Company
from catalog.models import Service
from invoice.utils import summ as to_words
from decimal import Decimal


class Invoice(models.Model):
	number = models.CharField(max_length=10, verbose_name="Номер счета")
	seller = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="seller", verbose_name="Продавец")
	buyer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="buyer", verbose_name="Покупатель")
	deel_date = models.DateField(auto_created=True, verbose_name="Дата составления")
	created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
	updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

	def total(self):
		sums = [s.sum() for s in self.items.all()]
		return sum(sums)

	def total_in_words(self):
		return to_words(self.total())

	def __str__(self):
		return self.buyer.name

	class Meta:
		verbose_name = u'Счет'
		verbose_name_plural = u'Счета'


class InvoiceItem(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items", verbose_name="Счет")
	service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
	quantity = models.IntegerField(default=1, verbose_name="Количество")
	price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")

	def sum(self):
		return Decimal(self.quantity) * Decimal(self.price)