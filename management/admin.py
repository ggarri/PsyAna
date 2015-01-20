from django.contrib import admin
from django.core.urlresolvers import reverse
from management.models import UserProfile, Office
# from tinymce.widgets import TinyMCE


class ProfileAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'last_login', 'date_joined', 'birthday')
    # ('Profile description',  {'fields': ['description'], 'widget': TinyMCE})


class OfficeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Office, OfficeeAdmin)
