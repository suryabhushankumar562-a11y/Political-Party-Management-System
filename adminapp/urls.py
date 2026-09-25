from django.urls import path

from .views import (
    AdminMemberListView,
    AdminMemberDetailView,
    AdminApproveMemberView,
    AdminRejectMemberView,
    AdminDashboardView,
    AdminLoginView,
    AdminLogoutView,
    AdminSuspendMemberView,
    AdminUnsuspendMemberView,

    AdminContactMessageListView,
    AdminContactMessageDetailView,

    AdminNewsListView,
    AdminNewsCreateView,
    AdminNewsUpdateView,
    AdminNewsDeleteView,

    AdminEventListView,
    AdminEventCreateView,
    AdminEventUpdateView,
    AdminEventDeleteView,

    AdminGalleryListView,
    AdminGalleryAddView,
    AdminGalleryEditView,
    AdminGalleryDeleteView,

    AdminLeaderListView,
    AdminLeaderCreateView,
    AdminLeaderUpdateView,
    AdminLeaderDeleteView,

    AdminManifestoListView,
    AdminManifestoCreateView,
    AdminManifestoUpdateView,
    AdminManifestoDeleteView,
)


urlpatterns = [

    # =========================================================
    # ADMIN LOGIN
    # =========================================================

    path(
        "login/",
        AdminLoginView.as_view(),
        name="admin_login"
    ),


    path(
        "logout/",
        AdminLogoutView.as_view(),
        name="admin_logout"
    ),

    # =========================================================
    # ADMIN DASHBOARD
    # =========================================================

    path(
        "",
        AdminDashboardView.as_view(),
        name="admin_dashboard"
    ),

    # =========================================================
    # MEMBERS MANAGEMENT
    # =========================================================

    path(
        "members/",
        AdminMemberListView.as_view(),
        name="admin_member_list"
        
    ),

    path(
        "members/<int:pk>/",
        AdminMemberDetailView.as_view(),
        name="admin_member_detail"
    ),

    path(
        "members/<int:pk>/approve/",
        AdminApproveMemberView.as_view(),
        name="admin_approve_member"
    ),

    path(
        "members/<int:pk>/reject/",
        AdminRejectMemberView.as_view(),
        name="admin_reject_member"
    ),

    path(
        "members/<int:pk>/suspend/",
        AdminSuspendMemberView.as_view(),
        name="admin_suspend_member"
    ),

    path(
        "members/<int:pk>/unsuspend/",
        AdminUnsuspendMemberView.as_view(),
        name="admin_unsuspend_member"
    ),

    # =========================================================
    # CONTACT MESSAGES
    # =========================================================

    path(
        "messages/",
        AdminContactMessageListView.as_view(),
        name="admin_contact_messages"
    ),

    path(
        "messages/<int:pk>/",
        AdminContactMessageDetailView.as_view(),
        name="admin_contact_message_detail"
    ),

    # =========================================================
    # NEWS MANAGEMENT
    # =========================================================

    path(
        "news/",
        AdminNewsListView.as_view(),
        name="admin_news_list"
    ),

    path(
        "news/add/",
        AdminNewsCreateView.as_view(),
        name="admin_news_add"
    ),

    path(
        "news/<int:pk>/edit/",
        AdminNewsUpdateView.as_view(),
        name="admin_news_edit"
    ),

    path(
        "news/<int:pk>/delete/",
        AdminNewsDeleteView.as_view(),
        name="admin_news_delete"
    ),

    # =========================================================
    # EVENT MANAGEMENT
    # =========================================================

    path(
        "events/",
        AdminEventListView.as_view(),
        name="admin_event_list"
    ),

    path(
        "events/add/",
        AdminEventCreateView.as_view(),
        name="admin_event_add"
    ),

    path(
        "events/<int:pk>/edit/",
        AdminEventUpdateView.as_view(),
        name="admin_event_edit"
    ),

    path(
        "events/<int:pk>/delete/",
        AdminEventDeleteView.as_view(),
        name="admin_event_delete"
    ),

    # =========================================================
    # GALLERY MANAGEMENT
    # =========================================================

    path(
        "gallery/",
        AdminGalleryListView.as_view(),
        name="admin_gallery_list"
    ),

    path(
        "gallery/add/",
        AdminGalleryAddView.as_view(),
        name="admin_gallery_add"
    ),

    path(
        "gallery/<int:pk>/edit/",
        AdminGalleryEditView.as_view(),
        name="admin_gallery_edit"
    ),

    path(
        "gallery/<int:pk>/delete/",
        AdminGalleryDeleteView.as_view(),
        name="admin_gallery_delete"
    ),

    # =========================================================
    # LEADERS MANAGEMENT
    # =========================================================

    path(
        "leaders/",
        AdminLeaderListView.as_view(),
        name="admin_leader_list"
    ),

    path(
        "leaders/add/",
        AdminLeaderCreateView.as_view(),
        name="admin_leader_add"
    ),

    path(
        "leaders/<int:pk>/edit/",
        AdminLeaderUpdateView.as_view(),
        name="admin_leader_edit"
    ),

    path(
        "leaders/<int:pk>/delete/",
        AdminLeaderDeleteView.as_view(),
        name="admin_leader_delete"
    ),

    # =========================================================
    # MANIFESTO MANAGEMENT
    # =========================================================

    path(
        "manifesto/",
        AdminManifestoListView.as_view(),
        name="admin_manifesto_list"
    ),

    path(
        "manifesto/add/",
        AdminManifestoCreateView.as_view(),
        name="admin_manifesto_add"
    ),

    path(
        "manifesto/<int:pk>/edit/",
        AdminManifestoUpdateView.as_view(),
        name="admin_manifesto_edit"
    ),

    path(
        "manifesto/<int:pk>/delete/",
        AdminManifestoDeleteView.as_view(),
        name="admin_manifesto_delete"
    ),

]