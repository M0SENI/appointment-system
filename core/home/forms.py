from django import forms
from .models import Appointments

class AppointmentForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Appointments
        fields = ['first_name', 'last_name', 'phone', 'request', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Request'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email



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