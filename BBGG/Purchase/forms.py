from django import forms

class PurchaseForm(forms.Form):
    USER_ID = forms.CharField()
    Amount = forms.IntegerField()
    Requirement = forms.CharField(max_length=255,required=False)
    Coupon_ID = forms.IntegerField(required=False)
class PurchaseForm2(forms.Form):
    Amount = forms.IntegerField()
    Requirement = forms.CharField(max_length=255,required=False)
    Coupon_ID = forms.IntegerField(required=False)