from django.contrib import admin

from .models import (News, Event, GalleryImage, Leader, ManifestoItem, ContactMessage,)

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "published",
        "created_at",
    )

    list_filter = (
        "category",
        "published",
    )

    search_fields = (
        "title",
        "short_description",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "event_time",
        "location",
        "published",
    )

    list_filter = (
        "published",
        "event_date",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    ordering = (
        "event_date",
    )


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "published",
        "created_at",
    )

    list_filter = (
        "published",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-created_at",
    )



@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "published",
        "order",
        "created_at",
    )

    list_filter = (
        "published",
    )

    search_fields = (
        "name",
        "designation",
    )

    ordering = (
        "order",
        "name",
    )


@admin.register(ManifestoItem)
class ManifestoItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "published",
        "created_at",
    )

    list_filter = (
        "published",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "order",
        "title",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )