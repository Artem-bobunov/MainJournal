from django.contrib import admin
from .models import InputJournal,Signature
# Register your models here.
from import_export.admin import ImportExportModelAdmin


class RegisterQuestion(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['numberInput', 'correspondent', 'content','executor','executionDate','mark','nomenklatura','signature']


class RegisterInputJournal(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['numberInput', 'user']

admin.site.register(InputJournal,RegisterQuestion)
admin.site.register(Signature,RegisterInputJournal)