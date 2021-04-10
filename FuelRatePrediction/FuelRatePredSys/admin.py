from django.contrib import admin
from .models import UserProfile, Pricing_Module

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Pricing_Module)





# Re-register UserAdmin