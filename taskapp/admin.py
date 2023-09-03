from django.contrib import admin
from .models import Profile, Task


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'firstname',
        'surname',
        'gate_code',
        'mobile_prefix',
        'mobile_number',
        'user'
    )
    list_filter = ('user', 'firstname', 'surname')
    search_fields = ['firstname', 'surname', 'user']
    actions = ['change_gate_code', 'new_mobile']

    def change_gate_code(self, request, queryset):
        queryset.update(gate_code='9876')

    def new_mobile(self, request, queryset):
        queryset.update(mobile_prefix='083', mobile_number='0830831')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('description',)}
    list_filter = ('created_by', 'category', 'completed', 'status')
    list_display = (
        'description',
        'status',
        'created_by',
        'completed',
        'category'
    )
    search_fields = [
        'completed',
        'description',
        'status',
        'category'
    ]
    actions = [
        'publish_task',
        'unpublish_task',
        'complete_task',
        'change_to_new'
    ]

    def publish_task(self, request, queryset):
        queryset.update(status=True)

    def unpublish_task(self, request, queryset):
        queryset.update(status=False)

    def complete_task(self, request, queryset):
        queryset.update(completed=True)

# sob : change_to_new is used for testing purposes
    def change_to_new(self, request, queryset):
        queryset.update(status=False, completed=False)
