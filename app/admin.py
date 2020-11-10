from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import JobPost, Cv

@admin.register(JobPost)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'company_name', 'vacency','emp_status', 'education_req', 'experiance_req', 'publish_date', 'application_deadline' )

    list_editable = ('application_deadline',)
    list_per_page = 2
    search_fields = ('job_name', 'company_name',)
    list_filter   = ('category','publish_date',)  

#@admin.register(Cv)
#Class CvAdmin(admin.ModelAdmin):
#    list_display = (__fields__) 	

# Register your models here

#admin.site.register(JobPost, JobAdmin)
admin.site.register(Cv)
#admin.site.unregister(Group)
#admin.site.unregister(User)
