from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    """ The Contact Us Form """

    class Meta:

        model = ContactUs
        fields = [
            "name",
            "email",
            "wedding",
            "subject",
            "message",
        ]

        labels = {
            "name": "Full Name",
            "wedding": "Tick box for Wedding Band Inquiry"
        }

        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Enter your full name",
            "email": "Enter your email address",
            "subject": "Enter the message subject",
            "message": "Enter your message",
        }
        excluded_fields = ["contact_reason", "message"]

        for field_name, field in self.fields.items():
            if field_name not in excluded_fields:
                field.widget.attrs["placeholder"] = placeholders.get(
                    field_name, "")
        self.fields["name"].widget.attrs["autofocus"] = True
