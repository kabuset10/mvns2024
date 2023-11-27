from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .models import Reading
from django.contrib.auth.models import User

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = [
            'motorist_first_name',
            'motorist_middle_initial',
            'motorist_last_name',
            'plate_number',
            'db_calculated',
            'db_reading',
            'distance_reading',
        ]
    def __init__(self, *args, **kwargs):
        super(ReadingForm, self).__init__(*args, **kwargs)
        self.fields['db_calculated'].required = False
        self.fields['db_reading'].required = False
        self.fields['distance_reading'].required = False

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]

class ChangePassForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']