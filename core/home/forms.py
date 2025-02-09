from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Appointments
        fields = ['first_name', 'last_name', 'phone', 'request', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام (به فارسی)' , 'id' : 'inputYourName' ,'require' : True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی(به فارسی)' , 'id' : 'inputYourLastName' , 'require' : True}),
            'phone': forms.TextInput(attrs={'class': 'form-control dz-number', 'placeholder': 'شماره تماس' , 'id' : 'inputYourPhone' , 'name':'dzPhoneNumber' , 'require' : True}),
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
        fields = ["first_name" , "last_name" ,'phone' ,'request',"status" , "note"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly" }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly" }),
            'phone': forms.TextInput(attrs={'class': 'form-control', "readonly": "readonly" }),
            'request': forms.Textarea(attrs={'class': 'form-control', "readonly": "readonly" }),
            'status': forms.Select(attrs={'class': 'form-control', }),
            "note": forms.Textarea(attrs={'class': 'form-control',}),
        }