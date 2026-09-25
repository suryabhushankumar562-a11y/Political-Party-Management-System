from django.contrib import admin
from django.utils import timezone

from .models import MemberProfile


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):

    list_display = (
        "membership_id",
        "get_username",
        "phone_number",
        "state",
        "district",
        "membership_status",
        "joining_date",
    )

    list_filter = (
        "membership_status",
        "gender",
        "state",
        "district",
    )

    search_fields = (
        "membership_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone_number",
    )

    readonly_fields = (
        "membership_id",
        "joining_date",
        "created_at",
        "updated_at",
        "approved_by",
        "approved_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20


    def get_username(self, obj):

        return obj.user.username

    get_username.short_description = "Username"


    def save_model(self, request, obj, form, change):

        if (
            obj.membership_status == "APPROVED"
            and obj.approved_by is None
        ):

            obj.approved_by = request.user
            obj.approved_at = timezone.now()

        elif obj.membership_status != "APPROVED":

            obj.approved_by = None
            obj.approved_at = None

        super().save_model(
            request,
            obj,
            form,
            change
        )