from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "title", "date", "content"]
    list_display_links = ["__str__", "title", "date", "content"]
    list_filter = ["date"]

    class Meta:
        model = Todo


admin.site.site_header = 'Todo Administration'
admin.site.register(Todo, TodoModelAdmin)
