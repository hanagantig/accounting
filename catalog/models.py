from django.db import models


class Service(models.Model):
	name = models.CharField(max_length=200, verbose_name="Название")
	price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Услуга'
		verbose_name_plural = u'Услуги'
