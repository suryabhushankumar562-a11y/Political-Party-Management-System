from django import forms

from members.models import MemberProfile
from cms.models import News, Event, GalleryImage, Leader, ManifestoItem



# =========================================================
# MEMBER REJECT FORM
# =========================================================

class MemberRejectForm(forms.ModelForm):

    class Meta:

        model = MemberProfile

        fields = ["remarks"]

        widgets = {

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": (
                        "Enter reason for rejecting this membership..."
                    ),
                }
            )

        }

        labels = {
            "remarks": "Reason for Rejection"
        }


    def clean_remarks(self):

        remarks = self.cleaned_data.get("remarks")

        if not remarks or not remarks.strip():

            raise forms.ValidationError(
                "Please provide a reason for rejection."
            )

        return remarks.strip()


# =========================================================
# ADMIN LOGIN FORM
# =========================================================

class AdminLoginForm(forms.Form):

    username = forms.CharField(
        label="Username",
        max_length=150,

        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter admin username",
                "autocomplete": "username",
            }
        )
    )


    password = forms.CharField(
        label="Password",

        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password",
                "autocomplete": "current-password",
            }
        )
    )


# =========================================================
# NEWS FORM
# =========================================================

class NewsForm(forms.ModelForm):

    class Meta:

        model = News

        fields = [
            "title",
            "category",
            "short_description",
            "content",
            "image",
            "published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter news title",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "short_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": (
                        "Write a short description of the news..."
                    ),
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": (
                        "Write the complete news content..."
                    ),
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "title": "News Title",

            "category": "Category",

            "short_description": "Short Description",

            "content": "Full Content",

            "image": "News Image",

            "published": "Publish this news",
        }




class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [
            "title",
            "description",
            "event_date",
            "event_time",
            "location",
            "image",
            "published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event title",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Enter event description",
                }
            ),

            "event_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "event_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event location",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "title": "Event Title",

            "description": "Description",

            "event_date": "Event Date",

            "event_time": "Event Time",

            "location": "Location",

            "image": "Event Image",

            "published": "Publish Event",
        }


class GalleryImageForm(forms.ModelForm):

    class Meta:

        model = GalleryImage

        fields = [
            "title",
            "image",
            "description",
            "published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter image title",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter image description...",
                }
            ),

            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "title": "Image Title",

            "image": "Gallery Image",

            "description": "Description",

            "published": "Publish Image",
        }


class LeaderForm(forms.ModelForm):

    class Meta:

        model = Leader

        fields = [
            "name",
            "designation",
            "profile_image",
            "bio",
            "order",
            "published",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter leader name",
                }
            ),

            "designation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter designation",
                }
            ),

            "profile_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Enter leader biography...",
                }
            ),

            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),

            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "name": "Leader Name",

            "designation": "Designation",

            "profile_image": "Profile Image",

            "bio": "Biography",

            "order": "Display Order",

            "published": "Publish Leader",
        }



class ManifestoItemForm(forms.ModelForm):

    class Meta:

        model = ManifestoItem

        fields = [
            "title",
            "description",
            "icon",
            "order",
            "published",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter manifesto title",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Enter manifesto description...",
                }
            ),

            "icon": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: bi bi-people",
                }
            ),

            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),

            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "title": "Manifesto Title",

            "description": "Description",

            "icon": "Icon",

            "order": "Display Order",

            "published": "Publish Item",
        }