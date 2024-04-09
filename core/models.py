from django.db import models
from user.models import User

class Order(models.Model):
   order_number = models.CharField(max_length=20, unique=True)
   customer = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.CharField(max_length=100)  
   total_price = models.DecimalField(max_digits=10, decimal_places=2)
   STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DELIVERED', 'Delivered'),
   )
        
   status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
   send_date = models.DateTimeField(auto_now_add=True)
   delivery_address = models.TextField()
   delivery_date = models.DateTimeField()

   def __str__(self):
        return f'Order {self.order_number} - Customer: {self.customer.username}'