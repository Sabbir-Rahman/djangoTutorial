from django import forms

from.models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 5,
                "cols": 20
            }
        ))
    price = forms.DecimalField(initial=120.25)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        #can use in any validation
        if not "sabbir" in title:
            raise forms.ValidationError("This is not a valid title you must contain sabbir word")
        if not "django" in title:
            raise forms.ValidationError("This is not a valid title you must contain django word")
        else:
            return title


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