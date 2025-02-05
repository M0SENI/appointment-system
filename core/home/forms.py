from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Appointment
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