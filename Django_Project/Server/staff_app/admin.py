from django.contrib import admin
from .models import Employee
from django.utils.html import format_html
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('show_photo', 'full_name', 'position', 'department', 'salary', 'date_hired')
    list_filter = ('order_number', 'client')
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                f'<img src="{obj.photo.url}" style="max-height: 100px;">')
            # можно и с использованием функции mark_safe
            # return mark_safe(
            # f'<img src="{obj.photo.url}" style="max-height: 100px;">')
        else:
            return "Фото не доступно"

    show_photo.short_description = 'Фото сотрудника'    