from django.contrib.auth import get_user_model
from django import forms


class VerifyForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' , 'name' : 'dzEmail' , 'placeholder' :  'ایمیل' , 'required' : True , 'type' : 'email'}))

class VerifyCodeForm(forms.Form):
    code = forms.CharField(max_length=6, widget=forms.Textarea(attrs={'class' : 'form-control' , 'required' : True , 'placeholder' : "کد شش رقمی"}))

class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control border-rounded'}), label='پسورد')
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control border-rounded'}), label='تایید پسورد')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('پسورد ها با هم برابر نیست!')
        return cleaned_data


