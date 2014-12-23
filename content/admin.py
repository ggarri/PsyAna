from django.contrib import admin
from django.core.urlresolvers import reverse
from content.models import UserProfile, Office
# from tinymce.widgets import TinyMCE


class ProfileAdmin(admin.ModelAdmin):
    pass
    # ('Profile description',  {'fields': ['description'], 'widget': TinyMCE})


class OfficeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Office, OfficeeAdmin)