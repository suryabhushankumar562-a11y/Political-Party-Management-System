from django import forms
from django.contrib.auth import get_user_model
from .models import MemberProfile
from django.db import transaction

User = get_user_model()


class MemberRegistrationForm(forms.ModelForm):

    # ----------------------------
    # CustomUser Fields
    # ----------------------------

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=True
    )

    username = forms.CharField(
        max_length=150,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )

    # ----------------------------
    # MemberProfile Model
    # ----------------------------

    class Meta:

        model = MemberProfile

        fields = [

            "profile_picture",

            "phone_number",

            "alternate_phone",

            "gender",

            "date_of_birth",

            "full_address",

            "state",

            "district",

            "city",

            "pincode",

        ]

        widgets = {

            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "full_address": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
            "class": "form-control"
        })

        self.fields["profile_picture"].widget.attrs.update({
            "class": "form-control"
    })

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                "confirm_password",
                "Passwords do not match."
            )

        if username:
            if User.objects.filter(username=username).exists():
                self.add_error(
                "username",
                "This username is already taken."
            )

        if email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    "email",
                    "This email is already registered."
                )

        return cleaned_data
    @transaction.atomic
    def save(self, commit=True):

    # MemberProfile object create (database me abhi save nahi hoga)
        member = super().save(commit=False)

    # CustomUser create
        user = User(
        username=self.cleaned_data["username"],
        first_name=self.cleaned_data["first_name"],
        last_name=self.cleaned_data["last_name"],
        email=self.cleaned_data["email"],
        role="MEMBER",
    )

    # Password hash
        user.set_password(self.cleaned_data["password"])

        if commit:

        # Save CustomUser
            user.save()

        # Link MemberProfile with CustomUser
        member.user = user

        # Save MemberProfile
        member.save()

        return member


class MemberLoginForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
                "autocomplete": "username",
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
            }
        )
    )


class MemberProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = MemberProfile

        fields = [
            "profile_picture",
            "phone_number",
            "alternate_phone",
            "gender",
            "date_of_birth",
            "full_address",
            "state",
            "district",
            "city",
            "pincode",
        ]

        widgets = {

            "profile_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),

            "alternate_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter alternate phone number",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "full_address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter your full address",
                }
            ),

            "state": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter state",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter district",
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter city",
                }
            ),

            "pincode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter pincode",
                }
            ),
        }
