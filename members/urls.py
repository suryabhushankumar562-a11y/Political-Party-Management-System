from django.urls import path

from .views import (
    MemberRegistrationView,
    MemberRegistrationSuccessView,
    MemberLoginView,
    MemberDashboardView,
    MemberLogoutView,
    MemberProfileUpdateView,
    MemberVerificationView,
    MemberMembershipCardView,

)

urlpatterns = [

    path(
        "register/",
        MemberRegistrationView.as_view(),
        name="member_register"
    ),

    path(
        "register/success/<str:membership_id>/",
        MemberRegistrationSuccessView.as_view(),
        name="member_register_success"
    ),

    path(
        "login/",
        MemberLoginView.as_view(),
        name="member_login"
    ),

    path(
        "dashboard/",
        MemberDashboardView.as_view(),
        name="member_dashboard"
    ),

    path(
        "logout/",
        MemberLogoutView.as_view(),
        name="member_logout"
    ),

    path(
    "profile/edit/",
    MemberProfileUpdateView.as_view(),
    name="member_profile_edit"
    ),

    path(
        "verify/<str:membership_id>/",
        MemberVerificationView.as_view(),
        name="member_verify"
    ),

    path(
        "membership-card/",
        MemberMembershipCardView.as_view(),
        name="member_membership_card"
    ),

]