"""Database settings of the 'Bookmarks' application."""

from django.conf import settings
from django.db import models

from core.enums import Limits


class UrlType(models.Model):
    """Url type model."""

    name = models.CharField(
        "name",
        max_length=Limits.URL_TYPE_NAME_MAX_LENGTH,
        help_text="url type name",
    )

    class Meta:
        verbose_name = "urltype"
        verbose_name_plural = "urltypes"

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Collection Model."""

    name = models.CharField(
        "name",
        unique=True,
        max_length=Limits.COLLECTION_NAME_MAX_LENGTH,
        help_text="collection's name",
    )
    description = models.CharField(
        "description",
        max_length=Limits.COLLECTION_DESCRIPTION_MAX_LENGTH,
        help_text="add a description of the collection",
    )
    time_created = models.DateTimeField(
        "date of creation",
        help_text="date the collection was created",
        auto_now_add=True,
    )
    time_updated = models.DateTimeField(
        "date of update",
        help_text="date of the last update of the collection",
        auto_now=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        help_text="author of the collection",
        on_delete=models.CASCADE,
        related_name="collections",
    )

    class Meta:
        verbose_name = "collection"
        verbose_name_plural = "collections"

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    """Bookmark Model."""

    title = models.CharField(
        "title",
        max_length=Limits.BOOKMARK_TITLE_MAX_LENGTH,
        help_text="bookmark page title",
    )
    description = models.CharField(
        "description",
        max_length=Limits.BOOKMARK_DESCRIPTION_MAX_LENGTH,
        help_text="add a description of the collection",
        blank=True,
        null=True,
    )
    url = models.URLField(
        "url",
        help_text="link to the page",
    )
    url_type = models.ForeignKey(
        UrlType,
        verbose_name="url type",
        help_text="link type",
        on_delete=models.PROTECT,
        related_name="bookmarks",
        default=1,
    )
    image = models.ImageField(
        "image",
        max_length=Limits.BOOKMARK_IMAGE_MAX_LENGTH,
        help_text="image preview",
        upload_to="bookmarks/images/",
    )
    time_created = models.DateTimeField(
        "date of creation",
        help_text="date the bookmark was created",
        auto_now_add=True,
    )
    time_updated = models.DateTimeField(
        "date of update",
        help_text="date of the last update of the bookmark",
        auto_now=True,
    )
    collections = models.ManyToManyField(
        Collection,
        verbose_name="collection",
        help_text="add a bookmark to the collections",
        related_name="bookmarks",
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        help_text="author of the bookmark",
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )

    class Meta:
        verbose_name = "bookmark"
        verbose_name_plural = "bookmarks"

    def __str__(self):
        return self.title
