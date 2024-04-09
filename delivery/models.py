from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeliveryCompletion(models.Model):
    service_provider=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='deliveries_provided')
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='deliveries_sent')
    order=models.ForeignKey('core.Order',on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
 
    def str(self):
      return f'DeliveryCompletion:Order{self.order.id}'
    

class PaymentInvoice(models.Model):
    delivery_completion = models.OneToOneField(DeliveryCompletion, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    sender_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=255)
    sender_contact = models.CharField(max_length=50)
    service_provider_name = models.CharField(max_length=100)
    service_provider_address = models.CharField(max_length=255)
    service_provider_contact = models.CharField(max_length=50)

    def __str__(self):
        return self.invoice_number
    
