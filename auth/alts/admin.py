from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    search_fields = ["email", "names"]
    list_display = ("email","first_name", "last_name",\
        "admin","active", "staff","buyer","employee",'non'
    )
    list_filter = ("admin", "active", "staff")
    fieldsets = (
        ("Basic", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name",)}),
        ("Permissions",{"fields": ("admin","active","staff", )},),
        ("Others",{"fields": ("buyer","employee",'non')},),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",),"fields": ("email","password1","password2",\
            "first_name", "last_name", "active","staff","admin","buyer","employee",),}, ),
    )
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)