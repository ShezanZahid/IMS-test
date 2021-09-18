
from django import forms

class MyForm(forms.Form): 
    region = forms.ChoiceField(initial={'max_number': '3'})
    product_code = forms.ChoiceField(initial={'max_number': '3'})
    #All my attributes here