from django.db import models



class ContactUs(models.Model):
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155, blank=True, null=True)
    email = models.EmailField(max_length=155)
    user_id = models.CharField(max_length=155)
    company_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=155)
    subject = models.CharField(max_length=155, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
