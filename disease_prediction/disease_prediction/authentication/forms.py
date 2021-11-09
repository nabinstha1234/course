from django import forms

from django.contrib.auth.forms import UserCreationForm
from disease_prediction.user.models import User, UserProfile



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=220)
    last_name = forms.CharField(max_length=220)
    is_active = forms.BooleanField(required=False)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

class UserProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField()
    store_name = forms.CharField(required=False)
    address = forms.CharField(required=False)
    zip = forms.CharField(required=False)
    b_firstname = forms.CharField(required=False)
    b_lastname = forms.CharField(required=False)
    user_status = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = [
            'b_firstname',
            'b_lastname',
            'phone',
            'store_name',
            'address',
            'zip'
        ]
