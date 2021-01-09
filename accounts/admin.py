from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, LoginForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = RegisterForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name', 'email',]

admin.site.register(CustomUser, CustomUserAdmin)