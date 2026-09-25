from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class AdminRequiredMixin(LoginRequiredMixin):

    login_url = "/admin-panel/login/"

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if request.user.role not in ["ADMIN", "SUPERADMIN"]:
            return redirect("member_dashboard")

        return super().dispatch(
            request,
            *args,
            **kwargs
        )