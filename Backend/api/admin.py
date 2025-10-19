from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Customize admin site headers
admin.site.site_header = "SkillSwap Administration"
admin.site.site_title = "SkillSwap Admin"
admin.site.index_title = "Welcome to SkillSwap Administration"

# Ensure User and Group are registered (they should be by default)
# This is just to make sure they're available
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)

if not admin.site.is_registered(Group):
    admin.site.register(Group)
