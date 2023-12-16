from django.db import models

class ContactUs(models.Model):

    """ Model for contact form / feedback """

    class Meta:
        verbose_name_plural = 'Contact-Us'

    CATEGORY_CHOICES = [
        ('Wedding', 'Wedding'),
        ('General', 'General'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General', null=False, blank=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name