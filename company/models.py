from django.db import models


# TODO: implement company type
class Company(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name="Наименование компании")
	inn = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name="ИНН")
	kpp = models.CharField(max_length=9, verbose_name="КПП")
	ogrn = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="ОГРН")
	# TODO: create cities app ???
	address = models.CharField(max_length=255, verbose_name="Адрес")
	owner = models.CharField(max_length=255, null=False, blank=False, verbose_name="ФИО руководителя",
							 help_text="Отображается в подписи")
	accountant = models.CharField(max_length=255, null=False, blank=False, verbose_name="ФИО главного бухгалтера",
								  help_text="Отображается в подписи")

	def get_account(self):
		return self.accounts.get()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Компания'
		verbose_name_plural = u'Компании'

