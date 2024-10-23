from django.shortcuts import render, redirect
from .forms import BillingForm

def billing_view(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            # Process the payment here (e.g., using Stripe or PayPal APIs)
            # You can save the form data to the database if needed

            return redirect('home')  # Redirect to a success page
    else:
        form = BillingForm()

    return render(request, 'billing/billing_form.html', {'form': form})