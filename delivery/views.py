from django.shortcuts import render, redirect
from .models import PaymentInvoice
from .forms import PaymentInvoiceForm

def create_invoice(request):
    if request.method == 'POST':
        form = PaymentInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')  # Redirect to invoice list page
    else:
        form = PaymentInvoiceForm()
    return render(request, 'invoice.html', {'form': form})

def invoice_list(request):
    invoices = PaymentInvoice.objects.all()
    return render(request, 'invoice_list.html', {'invoices': invoices})
