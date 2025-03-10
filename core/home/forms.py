from django import forms
from .models import Appointments , Contact

class AppointmentForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Appointments
        fields = ['first_name', 'last_name', 'phone','category', 'request', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام (به فارسی)' , 'id' : 'inputYourName' ,'require' : True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی(به فارسی)' , 'id' : 'inputYourLastName' , 'require' : True}),
            'phone': forms.TextInput(attrs={'class': 'form-control dz-number', 'placeholder': 'شماره تماس' , 'id' : 'inputYourPhone' , 'name':'dzPhoneNumber' , 'require' : True}),
            'category': forms.Select(attrs={'class': 'form-control text-secondary', 'id' : 'inputYourCat', 'require' : True}),
            'request': forms.Textarea(attrs={'class': 'form-control', 'placeholder':  'یادداشت' , 'id': 'inputYourRequest' , 'require' : True}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email


# not usable yet
class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ["first_name" , "last_name" ,'phone' ,'category','request',"status" ,'meet_date', "note"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly", 'id' : 'InputYourFirstName' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly" , 'id' : 'InputYourLastName'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly" , 'id' : 'InputYourPhone'}),
            'category': forms.Select(attrs={'class': 'form-control text-secondary', 'id' : 'inputYourCat', 'readonly' : True}),
            'request': forms.Textarea(attrs={'class': 'form-control', "readonly": "readonly" , 'id' : 'InputYourRequest'}),
            'status': forms.Select(attrs={'class': 'form-control text-secondary', 'id' : 'InputYourStatus'}),
            'meet_date' : forms.TextInput(attrs={'class': 'form-control', 'id' : 'InputYourMeet'}) ,
            'note': forms.Textarea(attrs={'class': 'form-control h-25', 'id' : 'InputYourNote'}),
        }

class VerifyForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder' :  'ایمیل' , 'required' : True , 'type' : 'email'}))


class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'request', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام (به فارسی)' , 'id' : 'inputYourName' ,'require' : True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی(به فارسی)' , 'id' : 'inputYourLastName' , 'require' : True}),
            'phone': forms.TextInput(attrs={'class': 'form-control dz-number', 'placeholder': 'شماره تماس' , 'id' : 'inputYourPhone' , 'name':'dzPhoneNumber' , 'require' : True}),
            'request': forms.Textarea(attrs={'class': 'form-control', 'placeholder':  'یادداشت' , 'id': 'inputYourRequest' , 'require' : True}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email