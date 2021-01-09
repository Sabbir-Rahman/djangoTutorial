from django import forms

from.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


#pure django form
class RawProductForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your description",
                "class": "new-class-name two",
                "id":  "my-id-for-textarea",
                "rows": 5,
                "cols": 20
            }
        ))
    price = forms.DecimalField(initial=120.25)