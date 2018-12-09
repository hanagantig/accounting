from django.contrib import admin
from document.models import Invoice, InvoiceItem
import pdfkit
from django.http import HttpResponse
from django.template import loader
import os


def print_invoice(modeladmin, request, queryset):
	template = loader.get_template('invoice.html')
	for invoice in queryset:
		context = {
			'invoice': invoice,
		}
		file_path = os.path.basename('out.pdf')
		options = {
			'page-size': 'A4',
			'dpi': 400,
		}
		pdfkit.from_string(template.render(context, request), 'out.pdf', options=options)
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read())
			response['Content-Type'] = 'application/force-download'
			file_name = 'schet N{}.{}'.format(invoice.number, 'pdf')
			response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
			response['X-Sendfile'] = os.path.basename(file_name)
			return response


def print_akt(modeladmin, request, queryset):
	template = loader.get_template('akt.html')
	for invoice in queryset:
		context = {
			'invoice': invoice,
		}
		file_path = os.path.basename('out.pdf')
		options = {
			'page-size': 'A4',
			'dpi': 400,
		}
		pdfkit.from_string(template.render(context, request), 'out.pdf', options=options)
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read())
			response['Content-Type'] = 'application/force-download'
			file_name = 'akt N{}.{}'.format(invoice.number, 'pdf')
			response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
			response['X-Sendfile'] = os.path.basename(file_name)
			return response


print_invoice.short_description = 'Скачать счет pdf'
print_akt.short_description = 'Скачать акт pdf'


class ItemsInline(admin.TabularInline):
	model = InvoiceItem
	extra = 1

	fields = ('service', 'quantity', 'price', 'sum')
	readonly_fields = ('sum',)

	def sum(self, obj):
		return float(obj.price) * float(obj.quantity)


class InvoiceAdmin(admin.ModelAdmin):
	inlines = [ItemsInline]
	actions = [print_invoice, print_akt]


admin.site.register(Invoice, InvoiceAdmin)
