from django.contrib import admin
from userauths.models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','gender']
    list_filter = ['username','email','gender']
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

