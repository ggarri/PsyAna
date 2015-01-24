from django.contrib import admin
from management.models import UserProfile, Office


class ProfileAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'last_login', 'date_joined', 'birthday', 'is_superuser')
    # actions = ['make_something']

    # def make_something(self, request, queryset):
    #     if not request.user.is_superuser:
    #         return queryset.update(request.user.id)

    # def get_queryset(self):
    #     if not self.request.user.is_superuser:
    #         return super(self).get_queryset().filter(id=self.request.user.id)
    #     else:
    #         return super(self).get_queryset()


class OfficeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Office, OfficeeAdmin)
