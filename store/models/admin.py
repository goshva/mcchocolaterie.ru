from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Post, PostAdmin)