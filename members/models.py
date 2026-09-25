from django.db import models
from django.conf import settings
from .utils import generate_membership_id
# Create your models here.

class MemberProfile(models.Model):

    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "other"),
    )

    STATUS_CHOICES = (
        ("PENDING" , "Pending"),
        ("APPROVED","Approved"),
        ("REJECTED", "Rejected"),
        ("SUSPENDED", "Suspended"),
        ("INACTIVE", "Inactive"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member_profile"
    )

    profile_picture = models.ImageField(
        upload_to="members/profile/",
        blank=True,
        null=True
    )

    phone_number = models.CharField(max_length=15,)

    alternate_phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    full_address = models.TextField()

    state = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    pincode = models.CharField(max_length=10)

    membership_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    joining_date = models.DateField(
        auto_now_add=True
    )

    membership_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    qr_code = models.ImageField(
        upload_to="members/qrcode/",
        blank=True,
        null=True
    )

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_members"
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
    blank=True,
    null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.membership_id:
            self.membership_id = generate_membership_id()
            

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} ({self.membership_id})"
