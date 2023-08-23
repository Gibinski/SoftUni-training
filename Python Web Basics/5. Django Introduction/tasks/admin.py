from django.contrib import admin
from tasks.models import Tasks


@admin.register()
class TaskAdmin(admin.ModelAdmin):
    pass
