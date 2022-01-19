from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
#
# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = CustomUser
#     list_display = ['pk', 'email', 'first_name', 'last_name', 'Created_date','Updated_date']
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('email', 'first_name', 'last_name','Created_date','Updated_date',)}),
#     )
#     fieldsets = UserAdmin.fieldsets
#
# admin.site.register(CustomUser, CustomUserAdmin)