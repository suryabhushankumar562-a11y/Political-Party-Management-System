from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .forms import MemberRegistrationForm, MemberLoginForm, MemberProfileUpdateForm
from .models import MemberProfile


# =========================================================
# MEMBER REGISTRATION
# =========================================================

class MemberRegistrationView(FormView):

    template_name = "members/register.html"
    form_class = MemberRegistrationForm

    def form_valid(self, form):

        member = form.save()

        messages.success(
            self.request,
            "Registration successful! Your membership request has been submitted."
        )

        self.success_url = reverse_lazy(
            "member_register_success",
            kwargs={
                "membership_id": member.membership_id
            }
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            "Please correct the errors below."
        )

        return super().form_invalid(form)


# =========================================================
# REGISTRATION SUCCESS
# =========================================================

class MemberRegistrationSuccessView(TemplateView):

    template_name = "members/register_success.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        membership_id = self.kwargs["membership_id"]

        member = MemberProfile.objects.get(
            membership_id=membership_id
        )

        context["member"] = member

        return context


# =========================================================
# MEMBER LOGIN
# =========================================================

class MemberLoginView(FormView):

    template_name = "members/login.html"
    form_class = MemberLoginForm

    success_url = reverse_lazy(
        "member_dashboard"
    )

    def form_valid(self, form):

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(
            self.request,
            username=username,
            password=password
        )

        if user is None:

            form.add_error(
                None,
                "Invalid username or password."
            )

            return self.form_invalid(form)

        if user.role != "MEMBER":

            form.add_error(
                None,
                "This login is only for members."
            )

            return self.form_invalid(form)

        login(
            self.request,
            user
        )

        messages.success(
            self.request,
            f"Welcome, {user.first_name or user.username}!"
        )

        return super().form_valid(form)


# =========================================================
# MEMBER DASHBOARD
# =========================================================

class MemberDashboardView(
    LoginRequiredMixin,
    TemplateView
):

    template_name = "members/dashboard.html"

    login_url = reverse_lazy(
        "member_login"
    )

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if request.user.role != "MEMBER":
            return redirect("admin_dashboard")

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        member = self.request.user.member_profile

        context["member"] = member

        return context


class MemberVerificationView(TemplateView):

    template_name = "members/verify.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        membership_id = self.kwargs["membership_id"]

        member = get_object_or_404(
            MemberProfile,
            membership_id=membership_id
        )

        context["member"] = member

        return context


class MemberProfileUpdateView(
    LoginRequiredMixin,
    FormView
):

    template_name = "members/edit_profile.html"
    form_class = MemberProfileUpdateForm

    success_url = reverse_lazy(
        "member_dashboard"
    )

    login_url = reverse_lazy(
        "member_login"
    )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.request.user.member_profile

        return kwargs

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Your profile has been updated successfully."
        )

        return super().form_valid(form)


# =========================================================
# MEMBER LOGOUT
# =========================================================

class MemberLogoutView(View):

    def get(
        self,
        request,
        *args,
        **kwargs
    ):

        logout(request)

        messages.success(
            request,
            "You have been logged out successfully."
        )

        return redirect(
            "member_login"
        )


class MemberMembershipCardView(
    LoginRequiredMixin,
    TemplateView
):

    template_name = "members/membership_card.html"

    login_url = reverse_lazy("member_login")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        member = get_object_or_404(
            MemberProfile,
            user=self.request.user
        )

        context["member"] = member

        return context
        