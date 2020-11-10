
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),    
    path('', include('django.contrib.auth.urls')),
]


#custmizing admin texts
admin.site.site_header = 'HRM'
admin.site.index_title = 'welcome to project'
admin.site.site_title  = 'control panel'
