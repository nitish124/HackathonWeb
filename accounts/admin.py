from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    #list_display let us modify the display in the table
    list_display = ('email', 'first_name', 'last_name', 'username', 'status', 'last_login', 'is_active', 'date_joined')

    #Display the attribute as a button
    list_display_links = ('email', 'first_name', 'last_name')

    #Make Fields read-only : last_login & date_joined cannot be editted
    readonly_fields = ('last_login', 'date_joined')

    #Ordering in descending Order from newer user to older
    ordering = ('-date_joined',)

    #Parameter to display a cutomUserModel 
    filter_horizontal = ()
    list_filter = ()
    #This will make the password read-only
    fieldsets = ()

admin.site.register(Account, AccountAdmin)