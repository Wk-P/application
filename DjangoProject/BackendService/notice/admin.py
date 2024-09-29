from django.contrib import admin
from notice.models import Notice, UserComment


# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('title', 'created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_at')
    search_fields = ('author',)
    list_filter = ('author', 'created_at', 'updated_at')

admin.site.register(Notice, NoticeAdmin)
admin.site.register(UserComment, CommentAdmin)