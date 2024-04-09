from django import forms
from . models import PaymentInvoice

class PaymentInvoiceForm(forms.ModelForm):
    class Meta:
        model=PaymentInvoice
        fields = ['invoice_number', 'invoice_date', 'due_date', 'seller_name', 'seller_address', 
                  'seller_contact', 'buyer_name', 'buyer_address', 'buyer_contact']