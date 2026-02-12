from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'phone_number', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('user__username', 'user__email', 'location', 'phone_number')
    readonly_fields = ('updated_at',)
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Profile Information', {
            'fields': ('Company', 'designation', 'profile_picture', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'location', 'website')
        }),
        ('Metadata', {
            'fields': ('updated_at',)
        }),
    )
