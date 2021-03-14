from django.contrib import admin
from .models import UserProfile, Pricing_Module

class Pricing_ModuleInLine(admin.TabularInline):
    model = Pricing_Module
    extra = 5

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['user']}),
    ('User Information',{'fields':['fullname','address','city','state','zipcode'],'classes':['collapse']}),]
    inlines = [Pricing_ModuleInLine]

#admin.site.register(UserProfile)
#admin.site.register(Pricing_Module)
admin.site.register(UserProfile,UserProfileAdmin)




