from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    menu_title      = "Users"
    list_display    = ['phone','email','username','role']
    list_per_page   = 100

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    menu_title      = "Users"
    list_display    = ['agent_id','account_type','user']
    list_per_page   = 100

@admin.register(Uccregister)
class UccregisterAdmin(admin.ModelAdmin):
    menu_title      = "Uccregister"
    list_display    = ['email','mobile','clint_code']
    list_per_page   = 100

    def clint_code(self, obj):
        if obj.param:
            return obj.param.get('clint_code', 'N/A')
        return 'N/A'
    clint_code.short_description = "Client Code"

@admin.register(Fatca)
class FatcaAdmin(admin.ModelAdmin):
    list_display = ['user', 'pan_number', 'invester_name']
    list_per_page   = 100

@admin.register(Mandate)
class MandateAdmin(admin.ModelAdmin):
    list_display = ['user', 'client_code', 'mandate_id']
    list_per_page = 100

@admin.register(Enach)
class EnachAdmin(admin.ModelAdmin):
    list_display = ['user', 'client_code', 'mandate_id']
    list_per_page = 100

@admin.register(XSIPTransaction)
class XSIPAdmin(admin.ModelAdmin):
    list_display = ['user', 'client_code', 'frequency_type']
    list_per_page = 100

@admin.register(AMCList)
class AMCListAdmin(admin.ModelAdmin):
    list_display = ['scheme_code', 'scheme_name', 'created_at']
    list_per_page = 100

    def scheme_code(self, obj):
        if obj.param and isinstance(obj.param, list) and len(obj.param) > 0:
            return obj.param[0].get('Scheme Code', 'N/A')
        return 'N/A'
    scheme_code.short_description = "Scheme Code"

    def scheme_name(self, obj):
        if obj.param and isinstance(obj.param, list) and len(obj.param) > 0:
            return obj.param[0].get('Scheme Name', 'N/A')
        return 'N/A'
    scheme_name.short_description = "Scheme Name"

@admin.register(AMCCart)
class AMCCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'scheme_code']
    list_per_page = 100