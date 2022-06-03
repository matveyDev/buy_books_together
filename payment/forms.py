from django import forms

class PaymentTagForm(forms.Form):
    amount = forms.IntegerField(required=True, label='Amount')