from django.contrib import admin
from .models import Task

# admin.site.register(Task)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('description',)}
    list_filter = ('status', 'created_by', 'category')
    list_display = ('description', 'status', 'created_by', 'category')
    search_fields = ['description', 'status', 'created_by', 'category']

    def publish_task(self, request, queryset):
        queryset.update(status=True)
