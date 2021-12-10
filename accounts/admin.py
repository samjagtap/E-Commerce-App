from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_display_links = ['email', 'first_name']
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined', )
    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
