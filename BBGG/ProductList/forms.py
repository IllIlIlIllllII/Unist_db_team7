from django import forms

class ProductForm(forms.Form):
    USER_ID = forms.CharField()
    Amount = forms.IntegerField()

class ProductForm2(forms.Form):
    Amount = forms.IntegerField()