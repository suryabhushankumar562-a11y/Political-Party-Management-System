from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
from django.views.generic.edit import FormView

from .forms import (
    MemberRejectForm,
    AdminLoginForm,
    NewsForm,
    EventForm,
    GalleryImageForm,
    LeaderForm,
    ManifestoItemForm,
)

from .mixins import AdminRequiredMixin

from members.models import MemberProfile

from cms.models import (
    News,
    Event,
    GalleryImage,
    Leader,
    ManifestoItem,
    ContactMessage,
)

# Create your views here.


class AdminMemberListView(
    AdminRequiredMixin,
    ListView
):

    model = MemberProfile

    template_name = "adminapp/members/list.html"

    context_object_name = "members"


    paginate_by = 3
    
    ordering = "-created_at"

    def get_queryset(self):

        queryset = MemberProfile.objects.select_related(
            "user"
        ).order_by("-id")

        status = self.request.GET.get("status", "").strip()

        search = self.request.GET.get("search", "").strip()

        if status:

            queryset = queryset.filter(
                membership_status=status
            )

        if search:

            queryset = queryset.filter(
                user__first_name__icontains=search
            ) | queryset.filter(
                user__last_name__icontains=search
            ) | queryset.filter(
                membership_id__icontains=search
            ) | queryset.filter(
                user__username__icontains=search
            )

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_members"] = MemberProfile.objects.count()

        context["pending_members"] = MemberProfile.objects.filter(
            membership_status="PENDING"
        ).count()

        context["approved_members"] = MemberProfile.objects.filter(
            membership_status="APPROVED"
        ).count()

        context["rejected_members"] = MemberProfile.objects.filter(
            membership_status="REJECTED"
        ).count()

        context["current_status"] = self.request.GET.get(
            "status",
            ""
        )

        context["search_query"] = self.request.GET.get(
            "search",
            ""
        )

        return context

class AdminMemberDetailView(AdminRequiredMixin, DetailView):

    model = MemberProfile

    template_name = "adminapp/members/detail.html"

    context_object_name = "member"

    

class AdminApproveMemberView(AdminRequiredMixin, View):

    

    def post(self, request, pk, *args, **kwargs):

        member = get_object_or_404(
            MemberProfile,
            pk=pk
        )

        member.membership_status = "APPROVED"
        member.approved_by = request.user
        member.approved_at = timezone.now()

        member.save(
            update_fields=[
                "membership_status",
                "approved_by",
                "approved_at",
                "updated_at",
            ]
        )

        messages.success(
            request,
            f"{member.membership_id} has been approved successfully."
        )

        return redirect(
            "admin_member_detail",
            pk=member.pk
        )


class AdminRejectMemberView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/members/reject.html"

    form_class = MemberRejectForm

    

    def dispatch(self, request, *args, **kwargs):

        self.member = get_object_or_404(
            MemberProfile,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["member"] = self.member

        return context

    def form_valid(self, form):

        self.member.membership_status = "REJECTED"

        self.member.remarks = form.cleaned_data["remarks"]

        self.member.approved_by = None
        self.member.approved_at = None

        self.member.save(
            update_fields=[
                "membership_status",
                "remarks",
                "approved_by",
                "approved_at",
                "updated_at",
            ]
        )

        messages.warning(
            self.request,
            f"{self.member.membership_id} has been rejected."
        )

        return redirect(
            "admin_member_detail",
            pk=self.member.pk
        )


class AdminDashboardView(
    AdminRequiredMixin,
    TemplateView
):

    template_name = "adminapp/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)


        # =========================================================
        # MEMBERS
        # =========================================================

        context["total_members"] = (
            MemberProfile.objects.count()
        )

        context["pending_members"] = (
            MemberProfile.objects
            .filter(membership_status="PENDING")
            .count()
        )

        context["approved_members"] = (
            MemberProfile.objects
            .filter(membership_status="APPROVED")
            .count()
        )

        context["rejected_members"] = (
            MemberProfile.objects
            .filter(membership_status="REJECTED")
            .count()
        )


        # =========================================================
        # RECENT MEMBERS
        # =========================================================

        context["recent_pending"] = (
            MemberProfile.objects
            .filter(membership_status="PENDING")
            .select_related("user")
            .order_by("-created_at")[:5]
        )

        context["recent_members"] = (
            MemberProfile.objects
            .select_related("user")
            .order_by("-created_at")[:5]
        )


        # =========================================================
        # NEWS
        # =========================================================

        context["total_news"] = (
            News.objects.count()
        )

        context["published_news"] = (
            News.objects
            .filter(published=True)
            .count()
        )

        context["draft_news"] = (
            News.objects
            .filter(published=False)
            .count()
        )


        # =========================================================
        # EVENTS
        # =========================================================

        context["total_events"] = (
            Event.objects.count()
        )

        context["published_events"] = (
            Event.objects
            .filter(published=True)
            .count()
        )

        context["draft_events"] = (
            Event.objects
            .filter(published=False)
            .count()
        )


        # =========================================================
        # GALLERY
        # =========================================================

        context["total_gallery"] = (
            GalleryImage.objects.count()
        )

        context["published_gallery"] = (
            GalleryImage.objects
            .filter(published=True)
            .count()
        )


        # =========================================================
        # LEADERS
        # =========================================================

        context["total_leaders"] = (
            Leader.objects.count()
        )

        context["published_leaders"] = (
            Leader.objects
            .filter(published=True)
            .count()
        )


        # =========================================================
        # MANIFESTO
        # =========================================================

        context["total_manifesto"] = (
            ManifestoItem.objects.count()
        )

        context["published_manifesto"] = (
            ManifestoItem.objects
            .filter(published=True)
            .count()
        )


        # =========================================================
        # CONTACT MESSAGES
        # =========================================================

        context["total_messages"] = (
            ContactMessage.objects.count()
        )

        context["unread_messages"] = (
            ContactMessage.objects
            .filter(is_read=False)
            .count()
        )

        context["read_messages"] = (
            ContactMessage.objects
            .filter(is_read=True)
            .count()
        )


        return context

class AdminContactMessageListView(
    AdminRequiredMixin,
    ListView
):

    model = ContactMessage

    template_name = "adminapp/messages/list.html"

    context_object_name = "messages"

    paginate_by = 10

    ordering = "-created_at"

    def get_queryset(self):

        return ContactMessage.objects.order_by(
            "-created_at"
        )


class AdminContactMessageDetailView(
    AdminRequiredMixin,
    DetailView
):

    model = ContactMessage

    template_name = "adminapp/messages/detail.html"

    context_object_name = "message"

    def get_object(self, queryset=None):

        message = super().get_object(queryset)

        # Automatically mark unread message as read
        if not message.is_read:

            message.is_read = True

            message.save(
                update_fields=["is_read"]
            )

        return message



class AdminLoginView(FormView):

    template_name = "adminapp/login.html"

    form_class = AdminLoginForm

    success_url = reverse_lazy("admin_dashboard")

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

        if user.role not in ["ADMIN", "SUPERADMIN"]:

            form.add_error(
                None,
                "You are not authorized to access the admin panel."
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


class AdminLogoutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)

        messages.success(
            request,
            "You have been logged out successfully."
        )

        return redirect("admin_login")


class AdminSuspendMemberView(
    AdminRequiredMixin,
    View
):

    def post(self, request, pk, *args, **kwargs):

        member = get_object_or_404(
            MemberProfile,
            pk=pk
        )

        member.membership_status = "SUSPENDED"

        member.save(
            update_fields=[
                "membership_status",
                "updated_at",
            ]
        )

        messages.warning(
            request,
            f"{member.membership_id} has been suspended."
        )

        return redirect(
            "admin_member_detail",
            pk=member.pk
        )


class AdminUnsuspendMemberView(
    AdminRequiredMixin,
    View
):

    def post(self, request, pk, *args, **kwargs):

        member = get_object_or_404(
            MemberProfile,
            pk=pk
        )

        member.membership_status = "APPROVED"

        member.save(
            update_fields=[
                "membership_status",
                "updated_at",
            ]
        )

        messages.success(
            request,
            f"{member.membership_id} has been activated again."
        )

        return redirect(
            "admin_member_detail",
            pk=member.pk
        )


    # =========================================================
# NEWS MANAGEMENT
# =========================================================

class AdminNewsListView(
    AdminRequiredMixin,
    ListView
):

    model = News

    template_name = "adminapp/news/list.html"

    context_object_name = "news_list"

    paginate_by = 10

    ordering = "-created_at"


class AdminNewsCreateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/news/form.html"

    form_class = NewsForm

    success_url = reverse_lazy(
        "admin_news_list"
    )

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "News has been added successfully."
        )

        return super().form_valid(form)


class AdminNewsUpdateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/news/form.html"

    form_class = NewsForm

    success_url = reverse_lazy(
        "admin_news_list"
    )

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        self.news = get_object_or_404(
            News,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )


    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.news

        return kwargs


    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "News has been updated successfully."
        )

        return super().form_valid(form)


class AdminNewsDeleteView(
    AdminRequiredMixin,
    View
):

    def post(
        self,
        request,
        pk,
        *args,
        **kwargs
    ):

        news = get_object_or_404(
            News,
            pk=pk
        )

        news.delete()

        messages.success(
            request,
            "News has been deleted successfully."
        )

        return redirect(
            "admin_news_list"
        )


class AdminEventListView(
    AdminRequiredMixin,
    ListView
):

    model = Event

    template_name = "adminapp/events/list.html"

    context_object_name = "events"

    paginate_by = 5

    def get_queryset(self):

        return (
            Event.objects
            .order_by("event_date", "event_time")
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_events"] = Event.objects.count()

        context["published_events"] = (
            Event.objects
            .filter(published=True)
            .count()
        )

        context["draft_events"] = (
            Event.objects
            .filter(published=False)
            .count()
        )

        return context



# =========================================================
# EVENT CREATE
# =========================================================

class AdminEventCreateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/events/form.html"

    form_class = EventForm

    success_url = reverse_lazy(
        "admin_event_list"
    )

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Event has been created successfully."
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            "Please correct the errors below."
        )

        return super().form_invalid(form)


# =========================================================
# EVENT UPDATE
# =========================================================

class AdminEventUpdateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/events/form.html"

    form_class = EventForm

    success_url = reverse_lazy(
        "admin_event_list"
    )

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        self.event = get_object_or_404(
            Event,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.event

        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(
            **kwargs
        )

        context["event"] = self.event

        return context

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Event has been updated successfully."
        )

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            "Please correct the errors below."
        )

        return super().form_invalid(form)


# =========================================================
# EVENT DELETE
# =========================================================

class AdminEventDeleteView(
    AdminRequiredMixin,
    View
):

    def post(
        self,
        request,
        pk,
        *args,
        **kwargs
    ):

        event = get_object_or_404(
            Event,
            pk=pk
        )

        title = event.title

        event.delete()

        messages.success(
            request,
            f'"{title}" has been deleted successfully.'
        )

        return redirect(
            "admin_event_list"
        )

# =========================================================
# GALLERY LIST
# =========================================================

class AdminGalleryListView(
    AdminRequiredMixin,
    ListView
):

    model = GalleryImage

    template_name = "adminapp/gallery/list.html"

    context_object_name = "gallery_images"

    paginate_by = 8

    def get_queryset(self):

        return (
            GalleryImage.objects
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(
            **kwargs
        )

        context["total_images"] = (
            GalleryImage.objects.count()
        )

        context["published_images"] = (
            GalleryImage.objects
            .filter(published=True)
            .count()
        )

        context["draft_images"] = (
            GalleryImage.objects
            .filter(published=False)
            .count()
        )

        return context

# =========================================================
# GALLERY ADD
# =========================================================

class AdminGalleryAddView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/gallery/form.html"

    form_class = GalleryImageForm

    success_url = reverse_lazy(
        "admin_gallery_list"
    )

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Gallery image has been added successfully."
        )

        return super().form_valid(form)


# =========================================================
# GALLERY EDIT
# =========================================================

class AdminGalleryEditView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/gallery/form.html"

    form_class = GalleryImageForm

    success_url = reverse_lazy(
        "admin_gallery_list"
    )

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        self.gallery_image = get_object_or_404(
            GalleryImage,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.gallery_image

        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(
            **kwargs
        )

        context["gallery_image"] = self.gallery_image

        context["is_edit"] = True

        return context

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Gallery image has been updated successfully."
        )

        return super().form_valid(form)


# =========================================================
# GALLERY DELETE
# =========================================================

class AdminGalleryDeleteView(
    AdminRequiredMixin,
    View
):

    def post(
        self,
        request,
        pk,
        *args,
        **kwargs
    ):

        gallery_image = get_object_or_404(
            GalleryImage,
            pk=pk
        )

        gallery_image.delete()

        messages.success(
            request,
            "Gallery image has been deleted successfully."
        )

        return redirect(
            "admin_gallery_list"
        )


    # =========================================================
# LEADERS LIST
# =========================================================

class AdminLeaderListView(
    AdminRequiredMixin,
    ListView
):

    model = Leader

    template_name = "adminapp/leaders/list.html"

    context_object_name = "leaders"

    paginate_by = 8

    def get_queryset(self):

        return (
            Leader.objects
            .order_by("order", "name")
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_leaders"] = (
            Leader.objects.count()
        )

        context["published_leaders"] = (
            Leader.objects
            .filter(published=True)
            .count()
        )

        context["draft_leaders"] = (
            Leader.objects
            .filter(published=False)
            .count()
        )

        return context


    # =========================================================
# ADD LEADER
# =========================================================

class AdminLeaderCreateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/leaders/form.html"

    form_class = LeaderForm

    success_url = reverse_lazy(
        "admin_leader_list"
    )

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Leader has been added successfully."
        )

        return super().form_valid(form)


# =========================================================
# EDIT LEADER
# =========================================================

class AdminLeaderUpdateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/leaders/form.html"

    form_class = LeaderForm

    success_url = reverse_lazy(
        "admin_leader_list"
    )

    def dispatch(self, request, *args, **kwargs):

        self.leader = get_object_or_404(
            Leader,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.leader

        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["leader"] = self.leader

        return context

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Leader has been updated successfully."
        )

        return super().form_valid(form)


# =========================================================
# DELETE LEADER
# =========================================================

class AdminLeaderDeleteView(
    AdminRequiredMixin,
    View
):

    def post(self, request, pk, *args, **kwargs):

        leader = get_object_or_404(
            Leader,
            pk=pk
        )

        leader_name = leader.name

        leader.delete()

        messages.success(
            request,
            f"{leader_name} has been deleted successfully."
        )

        return redirect(
            "admin_leader_list"
        )


    # =========================================================
# MANIFESTO LIST
# =========================================================

class AdminManifestoListView(
    AdminRequiredMixin,
    ListView
):

    model = ManifestoItem

    template_name = "adminapp/manifesto/list.html"

    context_object_name = "manifesto_items"

    paginate_by = 8

    def get_queryset(self):

        return (
            ManifestoItem.objects
            .order_by("order", "title")
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_manifesto"] = (
            ManifestoItem.objects.count()
        )

        context["published_manifesto"] = (
            ManifestoItem.objects
            .filter(published=True)
            .count()
        )

        context["draft_manifesto"] = (
            ManifestoItem.objects
            .filter(published=False)
            .count()
        )

        return context


# =========================================================
# ADD MANIFESTO
# =========================================================

class AdminManifestoCreateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/manifesto/form.html"

    form_class = ManifestoItemForm

    success_url = reverse_lazy(
        "admin_manifesto_list"
    )

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Manifesto item has been added successfully."
        )

        return super().form_valid(form)


# =========================================================
# EDIT MANIFESTO
# =========================================================

class AdminManifestoUpdateView(
    AdminRequiredMixin,
    FormView
):

    template_name = "adminapp/manifesto/form.html"

    form_class = ManifestoItemForm

    success_url = reverse_lazy(
        "admin_manifesto_list"
    )

    def dispatch(self, request, *args, **kwargs):

        self.manifesto = get_object_or_404(
            ManifestoItem,
            pk=kwargs["pk"]
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["instance"] = self.manifesto

        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["manifesto"] = self.manifesto

        return context

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Manifesto item has been updated successfully."
        )

        return super().form_valid(form)


# =========================================================
# DELETE MANIFESTO
# =========================================================

class AdminManifestoDeleteView(
    AdminRequiredMixin,
    View
):

    def post(self, request, pk, *args, **kwargs):

        manifesto = get_object_or_404(
            ManifestoItem,
            pk=pk
        )

        title = manifesto.title

        manifesto.delete()

        messages.success(
            request,
            f'"{title}" has been deleted successfully.'
        )

        return redirect(
            "admin_manifesto_list"
        )


    # =========================================================
# EVENT LIST
# =========================================================

class AdminEventListView(
    AdminRequiredMixin,
    ListView
):

    model = Event

    template_name = "adminapp/events/list.html"

    context_object_name = "events"

    paginate_by = 8

    def get_queryset(self):

        return (
            Event.objects
            .order_by("-event_date", "-event_time")
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_events"] = (
            Event.objects.count()
        )

        context["published_events"] = (
            Event.objects
            .filter(published=True)
            .count()
        )

        context["draft_events"] = (
            Event.objects
            .filter(published=False)
            .count()
        )

        return context