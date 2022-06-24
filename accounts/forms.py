from django import forms
from django.forms import widgets

from django.contrib.auth.models import User
from realtors.models import Realtor
from listings.models import Listing

# User Edit Form
class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Firstname'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Lastname'})
        self.fields['email'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Email'})

# Realtor Create Form
class RealtorForm(forms.ModelForm):
    
    class Meta:
        model = Realtor
        fields = ('name', 'photo', 'description', 'phone', 'email')
        exclude = ['is_mvp', 'hire_date']

        widgets = {
            'description':widgets.Textarea(attrs={'type':'textarea','name':'editor1', 'class': 'form-control rounded','rows':'5'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Full Name'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Phone'})
        self.fields['email'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Email'})

# Realtor Edit Form
class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ('title', 'realtor', 'address', 'city', 'state', 'zipcode', 'price', 'description', 'sqft', 'lot_size',
            'bedrooms', 'bathrooms', 'garage', 'photo_main', 'photo_1' , 'photo_2', 'photo_3', 'photo_4', 'photo_5', 
            'photo_5', 'photo_6'
        )
        exclude = ['is_published', 'list_date']

        widgets = {
            'description':widgets.Textarea(attrs={'type':'textarea','name':'editor1','class': 'form-control rounded','rows':'5'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Eg: 02 Kampala RD'})
        self.fields['realtor'].widget.attrs.update({'class': 'form-select input-md rounded'})
        self.fields['city'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'City'})
        self.fields['state'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'State'})
        self.fields['address'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Address'})
        self.fields['zipcode'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Zipcode'})
        self.fields['price'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Price'})
        self.fields['sqft'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Square Feet'})
        self.fields['lot_size'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Plot Size'})
        self.fields['bedrooms'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Bedrooms'})
        self.fields['bathrooms'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Bathrooms'})
        self.fields['garage'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'Garage(s)'})
        self.fields['photo_main'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})

        self.fields['photo_1'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['photo_2'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['photo_3'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['photo_4'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['photo_5'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
        self.fields['photo_6'].widget.attrs.update({'class': 'form-control rounded', 'placeholder': 'File'})
