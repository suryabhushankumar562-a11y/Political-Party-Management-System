from django.urls import path

from .views import (
    HomeView,
    AboutView,
    LeadershipView,
    NewsView,
    NewsDetailView,
    EventsView,
    EventDetailView,
    GalleryView,
    ManifestoView,
    DonateView,
    ContactView,
    ManifestoDetailView,

)


urlpatterns = [

    path(
        "",
        HomeView.as_view(),
        name="home"
    ),

    path(
        "about/",
        AboutView.as_view(),
        name="about"
    ),

    path(
        "leadership/",
        LeadershipView.as_view(),
        name="leadership"
    ),

    path(
        "news/",
        NewsView.as_view(),
        name="news"
    ),

    path(
        "news/<int:pk>/",
        NewsDetailView.as_view(),
        name="news_detail"
    ),

    path(
        "events/",
        EventsView.as_view(),
        name="events"
    ),

    path(
        "events/<int:pk>/",
        EventDetailView.as_view(),
        name="event_detail"
    ),

    path(
        "gallery/",
        GalleryView.as_view(),
        name="gallery"
    ),

    path(
        "manifesto/",
        ManifestoView.as_view(),

        name="manifesto"
    ),

    path(
        "donate/",
        DonateView.as_view(),

        name="donate"
    ),

    path(
        "contact/",
        ContactView.as_view(),
        name="contact"
    ),

    path(
        "manifesto/<int:pk>/",
        ManifestoDetailView.as_view(),
        name="manifesto_detail"
    ),

]