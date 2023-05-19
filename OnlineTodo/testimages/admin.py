from django.contrib import admin
from . models import Post,PostImages

# Register your models here.
class PostImageAdmin(admin.StackedInline):
    model = PostImages
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    class Meta:
        model=Post
@admin.register(PostImageAdmin)
class PostImageAdmin(admin.ModelAdmin):
    pass
