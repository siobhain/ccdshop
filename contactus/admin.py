from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):

    """ Display the Queries in the Admin Panel """

    list_display = (
        "created_on",
        "name",
        "email",
        "wedding",
        "subject",
        "message",
    )

    list_filter = ("created_on", "name", "wedding")

    ordering = ("-created_on",)


admin.site.register(ContactUs, ContactUsAdmin)
