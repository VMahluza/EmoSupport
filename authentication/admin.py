from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'is_online')
    list_filter = ('gender', 'is_online')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    readonly_fields = ('get_full_name',)
