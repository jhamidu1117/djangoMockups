from django.contrib import admin
from .models import FileTemplate, LiveReport, ReportFlows
# Register your models here.

admin.site.register(FileTemplate)
admin.site.register(LiveReport)
admin.site.register(ReportFlows)
