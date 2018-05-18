from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class ScRegistrationForm(forms.Form):
    ScName = forms.CharField(
        required = True,
        label = 'Service centre name',
        max_length = 32
    )
    ScEmailID = forms.CharField(
        required = True,
        label = 'EmailID',
        max_length = 32,
    )
    ScLocation = forms.CharField(
        required = True,
        label = 'Location',
        max_length = 200,
        )
    ScPhoneNum = forms.CharField(
        required = True,
        label = 'Phone number',
        max_length = 200,
        )
    Official = forms.BooleanField(
        required = True,
        label = 'Official',
        default = True,
        )
