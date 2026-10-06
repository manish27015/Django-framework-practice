from django.contrib import admin
from service.models import Service, ContactEnquiry

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(Service,ServiceAdmin)

from .models import ContactEnquiry


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'courses', 'message')