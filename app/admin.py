from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'owner')
    search_fields = ('title', 'description', 'owner__username', 'owner__email')
    ordering = ('-created_at',)
    list_select_related = ('owner',)
    date_hierarchy = 'created_at'

    actions = ('mark_completed', 'mark_uncompleted')

    @admin.action(description="علامت‌گذاری به‌عنوان انجام‌شده")
    def mark_completed(self, request, queryset):
        queryset.update(is_completed=True)

    @admin.action(description="برگرداندن به انجام‌نشده")
    def mark_uncompleted(self, request, queryset):
        queryset.update(is_completed=False)
