from django.contrib import admin
from .models import Joby


@admin.register(Joby)
class JobysAdmin(admin.ModelAdmin):
    list_display = [
        "customer_first_name",
        "customer_last_name",
        "customer_email",
        "project_date_request",
        "project_type", "status"
    ]
    list_display_links = "customer_first_name", "customer_email"
    ordering = '-id', 'project_date_request', 'status'
    list_per_page = 10
