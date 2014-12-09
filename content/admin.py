from django.contrib import admin
from django.core.urlresolvers import reverse
from content.models import Profile
# from tinymce.widgets import TinyMCE
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    (None,  {'fields': ['fullname']}),
    # ('Profile description',  {'fields': ['description'], 'widget': TinyMCE})

admin.site.register(Profile, ProfileAdmin)