from django.contrib import admin
from .models import Profile, Task

admin.site.register(Profile)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('description',)}
    list_filter = ('created_by', 'category', 'completed', 'status')
    list_display = ('description', 'status', 'created_by', 'completed', 'category')
    search_fields = ['completed', 'description', 'status', 'category']
    actions = ['publish_task', 'unpublish_task', 'complete_task', 'change_to_new']

    def publish_task(self, request, queryset):
        queryset.update(status=True)

    def unpublish_task(self, request, queryset):
        queryset.update(status=False)

    def complete_task(self, request, queryset):
        queryset.update(completed=True)

    def change_to_new(self, request, queryset):
        queryset.update(status=False, completed=False)
