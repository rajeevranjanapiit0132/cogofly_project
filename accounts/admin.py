from django.contrib import admin

from .models import User 


@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"] 
    list_filter = ["is_traveller", "is_staff", "is_superuser", "is_validated"]  
    search_fields = ["first_name", "last_name", "email"] 
  
    filter_horizontal = ["groups", "user_permissions"] 

    
