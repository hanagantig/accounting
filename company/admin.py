from django.contrib import admin
from company.models import Company
from account.models import Account


class AccounInline(admin.TabularInline):
	model = Account
	extra = 1


class CompanyAdmin(admin.ModelAdmin):
	inlines = [AccounInline]

admin.site.register(Company, CompanyAdmin)
