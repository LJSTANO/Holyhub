from django import forms
from django.core.validators import MinLengthValidator

from .models import Member
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

# Member Registration Form
class MemberRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,required=True,min_length=(8),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")

    class Meta:
        model = Member
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


# Member Login Form
class MemberLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)



# Member Update Form (for updating user info)
class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please provide a valid email address.")
        return email


# Member Delete Form (if needed for member removal)
class MemberDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm that I want to delete this member.")

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            raise forms.ValidationError("You must confirm before deleting a member.")
        return confirm

class PasswordResetEmailForm(forms.Form):
        email = forms.EmailField(label="Enter your email", required=True)

        def clean_email(self):
            email = self.cleaned_data.get('email')

            # Check if the email exists in the database
            try:
                member = Member.objects.get(email=email)
            except Member.DoesNotExist:
                raise ValidationError("No account found with this email address.")

            return email

class PasswordResetForm(forms.Form):
            new_password = forms.CharField(widget=forms.PasswordInput, label="New Password", required=True)
            confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", required=True)

            def clean(self):
                cleaned_data = super().clean()
                new_password = cleaned_data.get("new_password")
                confirm_password = cleaned_data.get("confirm_password")

                if new_password and confirm_password:
                    if new_password != confirm_password:
                        raise ValidationError("Passwords do not match.")
                return cleaned_data


