from django import forms
from django.forms import widgets 



class Registration_Form(forms.Form):
    First_Name = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control','name':'first_name','placeholder':'Enter the First Name'}))
    Last_Name = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control','name':'last_name','placeholder':'Enter the Last Name'}))
    email = forms.EmailField(widget=widgets.EmailInput(attrs={'class':'form-control','name':'email','placeholder':'Enter the Valid Email'}))
    username = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control','name':'last_name','placeholder':'Enter the username'}))
    password = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control','name':'last_name','placeholder':'Enter the Valid Password'}))
    ConfirmPassword = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control','name':'confirm_password','placeholder':'Enter the Confirm Password'}))


    def __init__(self, *args, **kwargs):
        super(Registration_Form, self).__init__(*args, **kwargs)
        self.fields['First_Name'].label = ""
        self.fields['Last_Name'].label = ""
        self.fields['email'].label = ""
        self.fields['username'].label = ""
        self.fields['password'].label = ""
        self.fields['ConfirmPassword'].label = ""


    def clean(self):

        cleaned_data = super(Registration_Form, self).clean()
        
        first_Name = cleaned_data.get('First_Name')
        last_Name = cleaned_data.get('Last_Name')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        if len(first_Name)<5:
            raise forms.ValidationError("First Name Minimum 5 characters required")

        if len(last_Name)<5:
            raise forms.ValidationError("Last Name Minimum 5 characters required")

        if len(email)<7:
            raise forms.ValidationError("Email Minimum 7 characters required")

        if len(username)<7:
            raise forms.ValidationError("UserName Minimum 7 characters required")
            

        # password validation
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('ConfirmPassword')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Password mismatch')

        return confirm_password


class Login_Form(forms.Form):
    username = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control','name':'username','placeholder':'Enter the UserName'}))
    password = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control','name':'password','placeholder':'Enter the Password'}))

    def __init__(self,*args,**kwargs):
        super(Login_Form,self).__init__(*args,**kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""

        