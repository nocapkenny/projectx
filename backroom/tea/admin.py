from django.contrib import admin
from tea.models import prepod, stud, faa, group, teoria


# Register your models here.

@admin.register(faa)
class FaaAdmin(admin.ModelAdmin):
    pass


@admin.register(prepod)
class PredopAdmin(admin.ModelAdmin):
    pass


@admin.register(stud)
class StudAdmin(admin.ModelAdmin):
    pass


@admin.register(group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(teoria)
class TeoriaAdmin(admin.ModelAdmin):
    pass

