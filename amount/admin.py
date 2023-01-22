from django.contrib import admin
from .models import Amount, Amount_list

class AmountpaidAdmin(admin.TabularInline):
  model = Amount_list
  fields=['Paid_To','Paid_fees']
  extra=0

  

class AmountAdmin(admin.ModelAdmin):
  fieldsets = (
    (('Personal info'), {'fields': ('user','Total_fees', 'Remaining_fees')}),    
  )
  inlines = [AmountpaidAdmin,]
  list_display = ['user','Total_fees', 'Remaining_fees']
  search_fields = ('user','Total_fees', 'Remaining_fees')
  ordering = ('user',)
  list_per_page = 10
admin.site.register(Amount, AmountAdmin)

# class MyMembershipInlineForm(forms.ModelForm):
#   class Meta:
#     model = MyUser.groups.through
#     fields = ("group", )
#     readonly_fields = (
#       "timestamp",
#       "size",
#     )
#   size = forms.IntegerField(disabled=True)

#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     my_membership = self.instance
#     self.initial = {
#       "size": my_membership.group.size if my_membership.pk else None
#     }

# class MyMembershipInline(admin.TabularInline):
#   model = MyMembership
#   fields = (
#     "group",
#     "user",
#   )
  # form = MyMembershipInlineForm

# class MyUserAdmin(admin.ModelAdmin):
#   fields = ("user_name",)
#   inlines = [MyMembershipInline]

# admin.site.register(MyUser, MyUserAdmin)