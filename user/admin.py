from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('username','email', 'password')}),
    (('Personal info'), {'fields': ('first_name', 'last_name','phone','gender')}),
    (('Fees_info'), {'fields': ('total_fees','Paid_fees','remaining_fees',)}),
    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
    (('Important dates'), {'fields': ('last_login', 'date_joined')}),       
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username','email', 'password1', 'password2','phone'),
      }),
  )
  list_display = ['username','email',"phone",'total_fees','Paid_fees','remaining_fees']
  search_fields = ('email', 'first_name', 'last_name','phone')
  ordering = ('email','phone','first_name' )
  list_per_page = 10
  

admin.site.register(CustomUser, UserAdmin)
