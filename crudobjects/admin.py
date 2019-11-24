from django.contrib import admin

from .models import Crudobject, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class CrudobjectAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = ("title", "author",)


admin.site.register(Crudobject, CrudobjectAdmin)