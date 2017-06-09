"""
This is not the content managment system you are looking for.
There aren't actually any "content" objects here (but do see the pages and boxes
apps) Instead, we treat content management as a set of attributes, and actions
around common "content management" tasks. These common attributes are:
    - automatic creation and updating dates
    - automatic tracking of a creator
    - access controls (TODO)
"""

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class ContentManageable(models.Model):
    created = models.DateTimeField(default=timezone.now, blank=True, db_index=True)
    updated = models.DateTimeField(blank=True)

    # We allow creator to be null=True so that we can, if we must, create a
    # ContentManageable object in a context where we don't have a creator (i.e.
    # where there isn't a request.user sitting around). However, we still leave
    # it blank=False so that any time we try to *validate* a ContentManageable
    # object we'll get an error. This is a reasonable compromise that lets us
    # track creators fairly well without neccisarily over-enforcing it in places
    # where it'd be invasive.
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_creator")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_modified")

    def save(self, **kwargs):
        self.updated = timezone.now()
        return super().save(**kwargs)

    class Meta:
        abstract = True


class NameSlugModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
