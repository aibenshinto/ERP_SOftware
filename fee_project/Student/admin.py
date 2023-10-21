from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import StudentForm, MasterData, Receipts
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.urls import path
from django.utils.safestring import mark_safe

class StudentFormAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.payment_type == 'One Time':
            obj.payment_type = MasterData.objects.filter(Name='One Time').first().value
            super().save_model(request, obj, form, change)
            Receipts.objects.create(student_form=obj, amount=obj.payment_type)
        elif obj.payment_type == 'Two Time':
            two_time_records = MasterData.objects.filter(Name='Two Time')
            values = [record.value for record in two_time_records]
            obj.payment_type = ', '.join(values)
            super().save_model(request, obj, form, change)
            for value in values:
                Receipts.objects.create(student_form=obj, amount=value)
        elif obj.payment_type == 'Three Time':
            two_time_records = MasterData.objects.filter(Name='Three Time')
            values = [record.value for record in two_time_records]
            obj.payment_type = ', '.join(values)
            super().save_model(request, obj, form, change)
            for value in values:
                Receipts.objects.create(student_form=obj, amount=value)

    def view_receipts_link(self, obj):
        receipts_url = reverse('admin:%s_%s_changelist' % (Receipts._meta.app_label,  Receipts._meta.model_name))
        return format_html('<a href="{}?student_form__id__exact={}">View Receipts</a>', receipts_url, obj.id)

    view_receipts_link.short_description = "Receipts"

    list_display = ['name', 'company', 'state', 'district', 'qualification', 'course', 'view_receipts_link']


class ReceiptsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        student_form_id = request.GET.get('student_form__id__exact')
        if student_form_id:
            qs = qs.filter(student_form_id=student_form_id)
        return qs

    def generate_pdf(self, request, receipt_id):
        receipt = self.get_object(request, receipt_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={receipt.student_form.name}_receipt.pdf'

        p = canvas.Canvas(response)
        p.drawString(100, 750, f'Name: {receipt.student_form.name}')
        p.drawString(100, 730, f'Company: {receipt.student_form.company}')
        p.drawString(100, 710, f'Qualification: {receipt.student_form.qualification}')
        p.drawString(100, 690, f'Course: {receipt.student_form.course}')
        p.drawString(100, 670, f'Receipt Number: {receipt.amount}')
        p.showPage()
        p.save()
        return response

    def generate_pdf_link(self, obj):
        pdf_url = reverse('admin:generate_pdf', args=[obj.pk])
        return format_html('<a href="{}">Generate PDF</a>', pdf_url)

    generate_pdf_link.allow_tags = True
    generate_pdf_link.short_description = 'PDF'

    list_display = [ 'student_form','amount', 'generate_pdf_link']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate_pdf/<int:receipt_id>/', self.generate_pdf, name='generate_pdf')
        ]
        return custom_urls + urls

admin.site.register(StudentForm, StudentFormAdmin)
admin.site.register(Receipts, ReceiptsAdmin)


        

    # def pdf_links(self, obj):
    #     # Assuming you have a function to generate PDF links
    #     # This function should generate and return a link to the PDF
    #     # using the obj.name and obj.payment_type
    #     return generate_pdf_link(obj.name, obj.payment_type)

    # list_display = ['name', 'company', 'state', 'district', 'qualification', 'course', 'pdf_links']
    # # ...












































# class ReceiptAdmin(admin.ModelAdmin):
   
#     actions = ['generate_receipt_pdf']


#     def view_pdf_link(self, obj):
#         return mark_safe(f'<a href="{reverse("admin:generate_pdf", args=[obj.id])}">View PDF</a>')

#     view_pdf_link.short_description = "View PDF"

#     def get_urls(self):
#         from django.urls import path

#         urls = super().get_urls()
#         custom_urls = [
#             path(
#                 'generate_pdf/<int:pk>/',
#                 self.admin_site.admin_view(self.generate_receipt_pdf_view),
#                 name='generate_pdf'
#             ),
#         ]
#         return custom_urls + urls


#     def generate_receipt_pdf_view(self, request, pk):
#         receipt = self.get_object(request, pk)
        
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="receipt_{pk}.pdf"'

#         p = canvas.Canvas(response)

#         student_form = receipt.student_form
#         payed_amount = receipt.payed_amount

#         p.drawString(100, 750, "Name: {}".format(student_form.name))
#         p.drawString(100, 730, "Payed Amount: {}".format(payed_amount))
#         p.showPage()

#         p.save()
#         return response

#     list_display = ['student_form', 'payed_amount', 'view_pdf_link']




# admin.site.register(StudentForm, StudentFormAdmin)
# admin.site.register(Receipts, ReceiptsAdmin)
# admin.site.register(Receipt, ReceiptAdmin)
# admin.site.register(Payment, Fee_typeAdmin)

