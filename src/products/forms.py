from django import forms

from .models import product

class productforms(forms.ModelForm):

    title       = forms.CharField(label='')
    description = forms.CharField(required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "class": "new-class-name two",
                                    "id": "my-des-id",
                                    "rows": 20,
                                    'cols':120
                                
                                }
                        )
                        
                        )
    price       = forms.FloatField()

    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price'
        ]
    #def clean_data(self, *args, **kwargs):
        #productforms = self.cleaned_data.get(id=15)
        #if not "CFE" in title:
            #raise forms.ValidationError("This is not a valid title")
        #return productforms

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "class": "new-class-name two",
                                    "id": "my-des-id",
                                    "rows": 20,
                                    'cols':120
                                }
                        )
                        
                        )
    price       = forms.FloatField()