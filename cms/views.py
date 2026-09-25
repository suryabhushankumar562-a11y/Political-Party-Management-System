from django.shortcuts import redirect, get_object_or_404
from .models import (News, Event, GalleryImage, Leader, ManifestoItem,)
from django.contrib import messages
from django.views.generic import TemplateView, DetailView

from .forms import ContactMessageForm

class HomeView(TemplateView):

    template_name = "cms/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["latest_news"] = (
            News.objects
            .filter(published=True)
            .order_by("-created_at")[:3]
        )

        context["upcoming_events"] = (
            Event.objects
            .filter(published=True)
            .order_by("event_date", "event_time")[:3]
        )

        context["leaders"] = (
            Leader.objects
            .filter(published=True)
            .order_by("order", "name")[:3]
        )

        context["gallery_images"] = (
            GalleryImage.objects
            .filter(published=True)
            .order_by("-created_at")[:4]
        )

        return context


class AboutView(TemplateView):

    template_name = "cms/about.html"


class LeadershipView(TemplateView):

    template_name = "cms/leadership.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["leaders"] = (
            Leader.objects
            .filter(published=True)
            .order_by("order", "name")
        )

        return context


class NewsView(TemplateView):

    template_name = "cms/news.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["news_list"] = (
            News.objects
            .filter(published=True)
            .order_by("-created_at")
        )

        return context


class EventsView(TemplateView):

    template_name = "cms/events.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["events"] = (
            Event.objects
            .filter(published=True)
            .order_by("event_date", "event_time")
        )

        return context


class EventDetailView(TemplateView):

    template_name = "cms/event_detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        event = get_object_or_404(
            Event,
            pk=self.kwargs["pk"],
            published=True
        )

        context["event"] = event

        return context


class GalleryView(TemplateView):

    template_name = "cms/gallery.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["gallery_images"] = (
            GalleryImage.objects
            .filter(published=True)
            .order_by("-created_at")
        )

        return context


class ManifestoView(TemplateView):

    template_name = "cms/manifesto.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["manifesto_items"] = (
            ManifestoItem.objects
            .filter(published=True)
            .order_by("order", "title")
        )

        return context


class ManifestoDetailView(DetailView):

    model = ManifestoItem

    template_name = "cms/manifesto_details.html"

    context_object_name = "manifesto"

    def get_queryset(self):
        return ManifestoItem.objects.filter(published=True)


class DonateView(TemplateView):

    template_name = "cms/donate.html"


class ContactView(TemplateView):

    template_name = "cms/contact.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["form"] = ContactMessageForm()

        return context

    def post(self, request, *args, **kwargs):

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully."
            )

            return redirect("contact")

        context = self.get_context_data(**kwargs)

        context["form"] = form

        return self.render_to_response(context)


class NewsDetailView(DetailView):

    model = News

    template_name = "cms/news_detail.html"

    context_object_name = "news"

    def get_queryset(self):

        return News.objects.filter(
            published=True
        )