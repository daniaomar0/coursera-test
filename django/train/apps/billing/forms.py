from django import forms

class BillingForm(forms.Form):
    card_number = forms.CharField(max_length=16, required=True)
    expiry_date = forms.CharField(max_length=5, required=True)
    cvc = forms.CharField(max_length=3, required=True)
    cardholder_name = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=100, required=True)
    address1 = forms.CharField(max_length=255, required=True)
    address2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=10, required=True)
    save_info = forms.BooleanField(required=False)
    terms = forms.BooleanField(required=True)