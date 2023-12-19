from django.db import models


class ContactUs(models.Model):

    """ Model for contact form / feedback """

    class Meta:
        verbose_name_plural = 'Contact-Us'

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    wedding = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
