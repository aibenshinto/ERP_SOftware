


from django.contrib import admin
from.models import Companies,State,District,Qualification,Courses,MasterData




class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['Company', 'Address1', 'Phone', 'Email', 'Website']

class StateAdmin(admin.ModelAdmin):
    list_display = ['state']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district', 'state']


class QualificationAdmin(admin.ModelAdmin):
    list_display = ['Qualificationname', 'Active']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['Course', 'Coursecode', 'Amount'] 


class MasterAdmin(admin.ModelAdmin):
    list_display = ['Name', 'value', 'type','Active'] 



# Register your models here.
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(MasterData,MasterAdmin)
