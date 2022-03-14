from pyexpat import model
from django.contrib import admin

# Register your models here.
from hakkillo.models import intent, organisation
from hakkillo.models import userprofile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(intent)
class intentAdmin(admin.ModelAdmin):
    list_display= ('tag', 'commentaire', 'pattern', 'response')
    pass

@admin.register(organisation)
class organisationAdmin(admin.ModelAdmin):
    list_display = ('nom_org', 'email', 'telephone', 'ville_org', 'pays')

class userprofileInline(admin.StackedInline):
    model = userprofile

class userprofileadmin(UserAdmin):
    inlines = (userprofileInline,)

admin.site.unregister(User)
admin.site.register(User, userprofileadmin)

