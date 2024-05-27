# -*- coding: windows-1251 -*-
from django.contrib import admin
from tea.models import faa, group, teoria, User, osenki

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(faa)
class FaaAdmin(admin.ModelAdmin):
    pass

@admin.register(group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(teoria)
class TeoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(osenki)
class OsenkiAdmin(admin.ModelAdmin):
    pass


