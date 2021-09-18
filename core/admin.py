from django.contrib import admin
from .models import Activenumber, Result
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ActivenumberResource(resources.ModelResource):

    class Meta:
        model = Activenumber    

class ActivenumberAdmin(ImportExportModelAdmin):
    resource_class = ActivenumberResource

class ResultResource(resources.ModelResource):

    class Meta:
        model = Result    

class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource

admin.site.register(Activenumber,ActivenumberAdmin)
admin.site.register(Result,ResultAdmin)